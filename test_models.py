from typing import Optional,List
from uuid import UUID,uuid4
from pydantic import BaseModel
from  enum import Enum


class User(BaseModel):
    id:Optional[UUID]=uuid4()
    first_name:str
    last_name:str