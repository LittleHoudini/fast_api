# FastAPI Routing Example

This project demonstrates a simple routing structure using **FastAPI**, organized into clear responsibility layers.

---

## Responsibility Layers

- **Repository Layer** → Communicates with the database and returns data.  
- **Service Layer** → Contains the business logic and core application rules.  
- **Controller Layer** → Handles incoming HTTP requests and responses.

---

## Run Locally

1. **Install dependencies:**
   ```bash
   uv sync
   ```

2. **Start the server (from the project root):**
   ```bash
   python -m uvicorn <folder_name>.main:app --host "localhost" --port 8001 --reload
   ```
