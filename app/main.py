from fastapi import FastAPI
from app.api import users

from app.infrastructure.database import engine, Base
from app.infrastructure import orm

async def create_tables():
    async with engine.begin() as conn:
        # Esto eliminará las tablas existentes y las volverá a crear.
        # ¡CUIDADO! En un entorno de producción real, usarías herramientas de migración como Alembic.
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

app = FastAPI()

@app.lifespan("startup")
async def on_startup():
    await create_tables()

app.include_router(users.router, prefix="/api/v1", tags=["Users"])


@app.get("/")
def read_root():
    return {"message": "Welcome to LinkHub API"}