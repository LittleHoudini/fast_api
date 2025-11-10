from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI, Request
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


def init_app(app: FastAPI, mongo_uri: str, db_name: str) -> None:
    """
    Attach a Motor client to app.state using FastApi lifespan
    """

    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
        app.state.mongo_client = AsyncIOMotorClient(mongo_uri)
        app.state.mongo_db_name = db_name
        yield
        app.state.mongo_client.close()

    app.router.lifespan_context = lifespan


def get_database(request: Request) -> AsyncIOMotorDatabase:
    client: AsyncIOMotorDatabase = request.app.state.mongo_client
    db_name: str = request.app.state.mongo_db_name
    return client[db_name]
