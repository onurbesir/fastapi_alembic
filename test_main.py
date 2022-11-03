from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI,HTTPException
from test_models import User

app = FastAPI()

db:List[User]=[
    User(
        id=uuid4(),
        first_name="test",
        last_name="lasttest"
    )
    ]

@app.get("/")
def root():
    return {"Hello","World"}

@app.get("/api/v1/users")
async def fetch_user():
    return db;

@app.post("/api/v1/users")
async def register_user(user:User):
    db.append(user)
    return {"id":user.id}

@app.delete("/api/v1/users/{user.id}")
async def delete_user(user_id:UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id :{user_id} does not exists"
    )
