from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    name: str
    surname: str
    age:int
    