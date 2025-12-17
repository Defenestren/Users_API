from fastapi import APIRouter, HTTPException
from db.client import fake_db
from db.models.user import User

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def get_users():
    return fake_db["users"]

@router.post("/")
def create_user(user: User):
    fake_db["users"].append(user)
    return user
