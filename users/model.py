from pydantic import BaseModel, ConfigDict, EmailStr, Field, model_validator


class UserBase(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=12,
    )
    email: EmailStr


class UserCreate(UserBase):
    model_config = ConfigDict(extra="ignore")
    password: str = Field(..., min_length=6, max_length=12)


class User(UserBase):
    uid: str
    password: str


class UserOut(UserBase):
    uid: str

    @model_validator(mode="before")
    @classmethod
    def convert_objectid(cls, data):
        if "_id" in data:
            data["uid"] = str(data["_id"])
            del data["_id"]
        return data
