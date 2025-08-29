# Clase en vídeo: https://youtu.be/_y9qQZXE24A

### Hola Mundo ###

# Documentación oficial: https://fastapi.tiangolo.com/es/

# Instala FastAPI: pip install "fastapi[all]"

# https://fastapi.tiangolo.com/es/tutorial/first-steps/?h=primeros+pasos


from fastapi import Cookie, FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from typing import Annotated
from fastapi.responses import PlainTextResponse
# import os

app = FastAPI()


# Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)

app.mount("/static", StaticFiles(directory="static"), name="static")
# Url local: http://127.0.0.1:8000/static/images/lago.jpg


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/video", response_class=HTMLResponse)
async def show_video():
    return """
    <html>
        <head>
            <title>Mi video</title>
        </head>
        <body style="display: flex; flex-direction: column; align-items: center; background-color: #111; color: white;">
            <h1>🎥 Reproduciendo Whitesnake</h1>
            <video id="myVideo" width="800" height="450" controls>
                <source src="/static/videos/ll_ltpwhitesnake_1.mp4" type="video/mp4">
                Tu navegador no soporta videos en HTML5.
            </video>
            <br>
            <button onclick="openFullscreen()">Pantalla completa</button>

            <script>
                var video = document.getElementById("myVideo");
                function openFullscreen() {
                    if (video.requestFullscreen) {
                        video.requestFullscreen();
                    } else if (video.webkitRequestFullscreen) { // Safari
                        video.webkitRequestFullscreen();
                    } else if (video.msRequestFullscreen) { // IE11
                        video.msRequestFullscreen();
                    }
                }
            </script>
        </body>
    </html>
    """


@app.get("/", response_class=PlainTextResponse)
async def root():
    return """¡Hola FastAPI!

url1:  https://users-api-ivu7.onrender.com/video/
url2:  https://users-api-ivu7.onrender.com/products/
url3:  https://users-api-ivu7.onrender.com/products/
url4:  https://users-api-ivu7.onrender.com/products/0/
url5:  https://users-api-ivu7.onrender.com/usersjson/
url6:  https://users-api-ivu7.onrender.com/users/1/
url7:  https://users-api-ivu7.onrender.com/users/usersquery/?id=1
url8:  https://users-api-ivu7.onrender.com/users/user/?id=1
url9:  https://users-api-ivu7.onrender.com/users/user/?id=1&name=Enrique
url10: https://users-api-ivu7.onrender.com/userdb/68b0174667180ac48cba2194
url11: https://users-api-ivu7.onrender.com/query/68b0174667180ac48cba2194
url12: https://users-api-ivu7.onrender.com/video/"""
# Url local: http://127.0.0.1:8000

@app.get("/url")
async def url():
    return {"url_curso": "https://bigrock.com/python"}
# Url local: http://127.0.0.1:8000/url


@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}


# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs

# Documentación con Redocly: http://127.0.0.1:8000/redoc




