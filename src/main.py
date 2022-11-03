from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .schemas import CreateUserRequest
from .database import get_db
from .models import User


app = FastAPI()


@app.get("/api/v1/users/get_all")
def get_all(db: Session = Depends(get_db)):
    return db.query(User).filter(User.id != None).all()


@app.get("/api/v1/users/get_by_id/{id}")
def get_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.id == id).first()
    

@app.post("/api/v1/users/create")
def create(details: CreateUserRequest, db: Session = Depends(get_db)):
    to_create = User(
        name=details.name,
        surname=details.surname,
        age=details.age
    )
    db.add(to_create)
    db.commit()
    return { 
        "success": True,
        "created_id": to_create.id
    }


@app.delete("/api/v1/users/delete/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    db.query(User).filter(User.id == id).delete()
    db.commit()
    return { "success": True }
