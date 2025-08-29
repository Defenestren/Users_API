# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=17664

### Users API con autorización OAuth2 JWT ###

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
# https://bcrypt-generator.com/
crypt = CryptContext(schemes=["bcrypt"])
SECRET = "201d573bd7d1344d3a3bfce1550b69102fd11be3db6d379508b6cccc58ea230b"

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
        "password": "$2a$12$KtYvf3OLW63oeEnr0OamjOy/u82qXkDz.HmLgsxUzRAy7Zvqv/R1a"},
    "lacheni": {
        "username": "lacheni",
        "full_name": "La Cheni",
        "email": "lacheni@gmail.com",
        "disabled": True,
        "password": "$2a$12$FXzFLRXzyjb7.oA6mznyqeHSgYdsQ9mWn6MMyUHxVOM3EDAvXLsXK"}
}


def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    

async def auth_user(token: str = Depends(oauth2)):

    exception = HTTPException(status.HTTP_401_UNAUTHORIZED,
                              detail = "Credenciales de autentificación inválidas.",
                              headers = {"WWW-Authenticate": "Bearer"})

    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception
        
    except JWTError:
        raise exception
    
    return search_user(username)


async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail = "Usuario inactivo.")
    return user


@router.post("/login1")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario no es correcto")
    user = search_user_db(form.username)
    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La contraseña no es correcta")
    access_token = {"sub": user.username,
                    "exp": datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_DURATION)}
    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}
#   Url local: http://127.0.0.1:8000/login1
#       Body > Form > Form Fields:
#           username : bigrock
#           password : 123456
#       Mensaje: {"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiaWdyb2NrIiwiZXhwIjoxNzU2Mjk1NDIzfQ.7Yn14H5IM0SjUolkNGFNxrxz5GymbIi5EkhctClF4Kg",
#                 "token_type": "bearer"}


@router.get("/users/me/me")
async def me(user: User = Depends(current_user)):
    return user
# http://127.0.0.1:8000/users/me/me
#   Auth > Bearer> Bearer Token:
#       eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiaWdyb2NrIiwiZXhwIjoxNzU2Mjk2NzQ1fQ.OhdiriGyWv2Io1HNG1iz0EV5OUcyF_HneuCfol1l8zc
#   Mensaje: {"username": "bigrock", "full_name": "Marcial Godes", "email": "MarcialGodes@gmail.com", "disabled": false}