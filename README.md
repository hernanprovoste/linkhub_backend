   git clone https://github.com/hernanprovoste/linkhub_backend.git
   cd linkhub_backend
   ```

2. **Install dependencies using Poetry:**

   ```bash
   poetry install
   ```

3. **Activate the virtual environment:**

   ```bash
   poetry shell
   ```

## Running the Application

To start the FastAPI development server:

```bash
uvicorn main:app --reload
```

The API documentation will be available at `http://127.0.0.1:8000/docs`.

## Project Structure
