Routing example using FastAPI

Responsibility layers:
    Repository layer -> talk to the DB, return whatever is there.
    Service layer -> Business logic:
    Controller -> Handles HTTP requests:

Run Locally:
    Install dependencies:
        uv sync
    Start the server with uvicorn (from project root):
        python -m uvicorn <folder_name>.main:app --host "localhost" --port 8001 --reload 