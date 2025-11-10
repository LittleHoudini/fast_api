from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends, HTTPException

from ..db import get_database
from .model import UserCreate, UserOut
from .service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=UserOut, status_code=HTTPStatus.OK)
async def create_user_endpoint(
    payload: UserCreate, db=Depends(get_database)
) -> UserOut:
    svc = UserService(db=db)
    return await svc.create_user(payload=payload)


@router.get("", response_model=List[UserOut])
async def list_users_endpoint(db=Depends(get_database)) -> List[UserOut]:
    svc = UserService(db=db)
    return await svc.get_all_users()


@router.get("/{user_id}", response_model=UserOut)
async def get_user_by_id_endpoint(user_id: str, db=Depends(get_database)) -> UserOut:
    svc = UserService(db=db)
    user = await svc.get_user_by_id(user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f"User with id={user_id} does not exist",
        )
    return user
