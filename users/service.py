from typing import List, Optional

from ..repositories.user_repo import UserRepository
from ..utils import str_to_oid
from .model import User, UserCreate, UserOut


class UserService:
    def __init__(self, db):
        self.repo = UserRepository(db)

    async def create_user(self, payload: UserCreate) -> User:
        new_id = await self.repo.create_user(data=payload)
        doc = await self.repo.get_user_by_id(user_id=str_to_oid(new_id))
        return UserOut(**doc)

    async def get_all_users(self) -> List[UserOut]:
        docs = await self.repo.get_all_users()
        return [UserOut(**d) for d in docs]

    async def get_user_by_id(self, user_id: str) -> Optional[UserOut]:
        user_id = str_to_oid(user_id)
        if user_id is None:
            return None
        doc = await self.repo.get_user_by_id(user_id=user_id)
        if not doc:
            return None
        return UserOut(**doc)
