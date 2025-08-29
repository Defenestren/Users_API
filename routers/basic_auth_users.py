# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=14094


### Users API con autorización OAuth2 básica ###

from fastapi import APIRouter, Depends, HTTPException, status, APIRouter
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


router = APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {
    "bigrock": {
        "username": "bigrock",
        "full_name": "Marcial Godes",
        "email": "MarcialGodes@gmail.com",
        "disabled": False,
        "password": "123456"},
    "lacheni": {
        "username": "lacheni",
        "full_name": "La Cheni",
        "email": "lacheni@gmail.com",
        "disabled": True,
        "password": "654321"}
}


def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    

async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,
                            detail = "Credenciales de autentificación inválidas.",
                            headers = {"WWW-Authenticate": "Bearer"})
    if user.disabled:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail = "Usuario inactivo.")
    return user


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
    return {"access_token": user.username, "token_type": "bearer"}
#   Url local: http://127.0.0.1:8000/login
#       Body > Form > Form Fields:
#           username : bigrock
#           password : 123456
#       Mensaje: {"access_token": "bigrock", "token_type": "bearer"}


@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
# http://127.0.0.1:8000//users/me
#   Auth > Bearer> Bearer Token:
#       bigrock
#   Mensaje: {"access_token": "bigrock", "token_type": "bearer"}