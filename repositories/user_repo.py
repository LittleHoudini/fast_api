from typing import List, Optional

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase

from ..users.model import UserCreate


class UserRepository:
    def __init__(self, db: AsyncIOMotorDatabase):
        self._col = db["users"]

    async def create_user(self, data: UserCreate) -> str:
        payload = data.model_dump()
        res = await self._col.insert_one(payload)
        return str(res.inserted_id)

    async def get_user_by_id(self, user_id: ObjectId) -> Optional[dict]:
        return await self._col.find_one({"_id": user_id})

    async def get_all_users(self) -> List[dict]:
        cursor = self._col.find({})
        return [doc async for doc in cursor]
