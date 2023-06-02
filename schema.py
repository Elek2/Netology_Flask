from pydantic import BaseModel, validator


class CreateUser(BaseModel):
    username: str
    email: str

    @validator("password")
    def password_len(cls, value):
        if len(value) < 5:
            raise ValueError("Password is too short")
