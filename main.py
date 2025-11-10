from pathlib import Path

from fastapi import FastAPI

from . import db as db_module
from .config.config import Config
from .users.controller import router as users_router

config_path = Path(__file__).parent.resolve() / "config/config.yaml"


config = Config(config_path=config_path)
db_data = config.get_item("database")
user, password, port, db_name = (
    db_data["mongo_user"],
    db_data["mongo_password"],
    db_data["mongo_port"],
    db_data["DB_NAME"],
)
MONGO_URI = f"mongodb://{user}:{password}@localhost:{port}"

app = FastAPI(title="Users Routing", docs_url="/api")
db_module.init_app(app, mongo_uri=MONGO_URI, db_name=db_name)
app.include_router(users_router)
