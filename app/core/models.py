from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class LinkBase(BaseModel):
    title: str
    url: str

class LinkCreate(LinkBase):
    pass

class Link(LinkBase):
    id: int
    user_id: int
    created_at: datetime
    is_active: bool

    model_config = ConfigDict(from_attributes=True)

class UserBase(BaseModel):
    email: str
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    links: list[Link] = []

    model_config = ConfigDict(from_attributes=True)