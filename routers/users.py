from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"message": "No encontrado"}}
)


router_2 = APIRouter()


class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1,
                   name="Enrique",
                   surname="Godes",
                   url="https://enrique.dev",
                   age=64),
              User(id=2,
                   name="Marcial",
                   surname="Godes",
                   url="https://marcial.com",
                   age=49),
              User(id=3,
                   name="Hakoon",
                   surname="Dahlberg",
                   url="https://haakon.com",
                   age=33)]


# Operación¶
# "Operación" aquí se refiere a uno de los "métodos" HTTP.

# Uno de:

# POST
# GET
# PUT
# DELETE
# ...y los más exóticos:

# OPTIONS
# HEAD
# PATCH
# TRACE
# En el protocolo HTTP, puedes comunicarte con cada path usando uno (o más) de estos "métodos".

# Al construir APIs, normalmente usas estos métodos HTTP específicos para realizar una acción específica.

# Normalmente usas:

# POST: para crear datos.
# GET: para leer datos.
# PUT: para actualizar datos.
# DELETE: para eliminar datos.
# Así que, en OpenAPI, cada uno de los métodos HTTP se llama una "operation".


# Inicia el server: uvicorn users:app --reload
@router.get("/usersjson/")
async def usersjson():
    return [{"id": 1, "name": "Enrique", "surname": "Godes", "url": "https://enrique.dev", "age": 64},
            {"id": 2,"name": "Marcial","surname": "Godes","url": "https://marcial.com","age": 49},
            {"id": 3,"name": "Hakoon","surname": "Dahlberg","url": "https://haakon.com","age": 33}]
# Url local: http://127.0.0.1:8000/users/usersjson/


@router.get("/")
async def users():
    return users_list
# Url local: http://127.0.0.1:8000/users


# Path
@router.get("/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}
# Url local: http://127.0.0.1:8000/users/1
# Url local: http://127.0.0.1:8000/users/2
# Url local: http://127.0.0.1:8000/users/3
# Url local: http://127.0.0.1:8000/users/4
# Url local: http://127.0.0.1:8000/user/...


# Query
@router.get("/usersquery/")
async def user(id: int):
    return search_user(id)
# Url local: http://127.0.0.1:8000/users/usersquery/?id=1
# Url local: http://127.0.0.1:8000/users/usersquery/?id=2
# Url local: http://127.0.0.1:8000/users/usersquery/?id=3
# Url local: http://127.0.0.1:8000/users/usersquery/?id=4
# Url local: http://127.0.0.1:8000/users/usersquery/?id=5
# Url local: http://127.0.0.1:8000/users/usersquery/?id=Marcial   # 422 Unprocessable Content
#   Error: Input should be a valid integer, unable to parse string as an integer


@router.get("/user/")
async def user(id: int):
    return search_user(id)
# Url local: http://127.0.0.1:8000/users/user/?id=1
# Url local: http://127.0.0.1:8000/users/user/?id=2
# Url local: http://127.0.0.1:8000/users/user/?id=3
# Url local: http://127.0.0.1:8000/users/user/?id=4

@router.get("/user/")
async def user(id: int, name: str):
    return search_user(id)
# Url local: http://127.0.0.1:8000/users/user/?id=1&name=Enrique
# Url local: http://127.0.0.1:8000/users/user/?id=2&name=Marcial
# Url local: http://127.0.0.1:8000/users/user/?id=3&name=Hakoon
# Url local: http://127.0.0.1:8000/users/user/?id=4&name=Enrique


@router.post("/user/", response_model=User, status_code=201)
async def create_user(user: User):

    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404,
                            detail="error: El usuario ya existe.")

    users_list.append(user)
    return user
# Url local: http://127.0.0.1:8000/users/user/
# Thunder client:
#   Url local: http://127.0.0.1:8000/users/user/
#       Body:
#           {"id": 4, "name": "LaCheni","surname": "LaCheni","url": "https://lacheni.com","age": 40}
#   Url local: http://127.0.0.1:8000/users/user/
#       Body:
#           {"id": 4, "name": "LaCheni","surname": "LaCheni","url": "https://lacheni.com","age": 40}
#           Mensaje: "error": "El usuario ya existe."


@router.put("/user/")
async def update_user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):

        if saved_user.id == user.id:
            users_list[index] = user
            found = True
  
    if not found:
        raise HTTPException(status_code=404,detail="error: No se ha actualizado el usuario.")
    
    return user
# Thunder client:
#   Url local: http://127.0.0.1:8000/users/user/
#       Body:
#           {"name": "LaCheni","surname": "LaCheni","url": "https://lacheni.com","age": 18}
#           Mensaje: 422 Unprocessable Content ("loc": ["body", "id"])
#       Body:
#           {"id": 5, "name": "LaCheni","surname": "LaCheni","url": "https://lacheni.com","age": 18}
#           Mensaje:   "error": "No se ha actualizado el usuario."
#       Body:
#           {"id": 4, "name": "LaCheni","surname": "LaCheni","url": "https://lacheni.com","age": 18}


@router.delete("/user/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):

        if saved_user.id == id:
            del users_list[index]
            found = True
            return {"El usuario ha sido eliminado."}

    if not found:
        raise HTTPException(status_code=404,detail="error: No se ha eliminado el usuario.")
# Url local: http://127.0.0.1:8000/users/user/4
#   Se elimina el usuario con id: 4. Mensaje: "El usuario ha sido eliminado."
# Url local: http://127.0.0.1:8000/users/user/4
#   No se Elimina el usuario ya que no hay ninguno con id: 4. Mensaje: "error": "No se ha eliminado el usuario."


def search_user(id: int):

    users = filter(lambda user: user.id == id, users_list)
    
    try:
        return list(users)[0]
    
    except:
        return {"error": "No se ha encontrado el usuario"}
        # raise HTTPException(status_code=404,detail="error: No se ha encontrado el usuario.")
    

# https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Status

# Respuestas informativas:
#   ■ 100 Continue (https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Status/100)
#     Esta respuesta provisional indica que todo hasta ahora está bien y que el cliente debe continuar
#     con la solicitud o ignorarla si ya está terminada.


# Respuestas satisfactorias:
#   ■ 200 OK (https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Status/200)
#     La solicitud ha tenido éxito. El significado de un éxito varía dependiendo del método HTTP:

#   ■ 201 Created (https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Status/201)
#     La solicitud ha tenido éxito y se ha creado un nuevo recurso como resultado de ello.
#     Ésta es típicamente la respuesta enviada después de una petición PUT.

#   ■ 202 Accepted (https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Status/202)
#     La solicitud se ha recibido, pero aún no se ha actuado. Es una petición "sin compromiso",
#     lo que significa que no hay manera en HTTP que permite enviar una respuesta asíncrona que indique el
#     resultado del procesamiento de la solicitud. Está pensado para los casos en que otro proceso
#     o servidor maneja la solicitud, o para el procesamiento por lotes.

#   ■ 203 Non-Authoritative Information (https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Status/203)
#     La petición se ha completado con éxito, pero su contenido no se ha obtenido de la fuente originalmente
#     solicitada, sino que se recoge de una copia local o de un tercero. Excepto esta condición,
#     se debe preferir una respuesta de 200 OK en lugar de esta respuesta.

#   ■ 204 No Content (https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/204)
#     La petición se ha completado con éxito pero su respuesta no tiene ningún contenido, aunque los encabezados
#     pueden ser útiles. El agente de usuario puede actualizar sus encabezados en caché para este recurso
#     con los nuevos valores.


# Redirecciones:
#   ■ 300 Multiple Choice (https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/300)
#     Esta solicitud tiene más de una posible respuesta. User-Agent o el usuario debe escoger uno de ellos.
#     No hay forma estandarizada de seleccionar una de las respuestas.

#   ■ 301 Moved Permanently (https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/301)
#     Este código de respuesta significa que la URI del recurso solicitado ha sido cambiado.
#     Probablemente una nueva URI sea devuelta en la respuesta.

#   ■ 302 Found (https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Status/302)
#     Este código de respuesta significa que el recurso de la URI solicitada ha sido cambiado temporalmente.
#     Nuevos cambios en la URI serán agregados en el futuro. Por lo tanto, la misma URI debe ser usada
#     por el cliente en futuras solicitudes.

#   ■ 303 See Other (https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/303)
#     El servidor envía esta respuesta para dirigir al cliente a un nuevo recurso solicitado a otra dirección
#     usando una petición GET.

#   ■ 304 Not Modified (https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Status/304)
#     Esta es usada para propósitos de "caché". Le indica al cliente que la respuesta no ha sido modificada.
#     Entonces, el cliente puede continuar usando la misma versión almacenada en su caché.


# Errores de cliente
#   ■ 400 Bad Request (https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Status/400)
#     Esta respuesta significa que el servidor no pudo interpretar la solicitud dada una sintaxis inválida.

#   ■ 401 Unauthorized (https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Status/401)
#     Es necesario autenticar para obtener la respuesta solicitada. Esta es similar a 403, pero en este caso,
#     la autenticación es posible.

#   ■ 402 Payment Required (https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Status#402_payment_required)
#     Este código de respuesta está reservado para futuros usos. El objetivo inicial de crear este código fue
#     para ser utilizado en sistemas digitales de pagos. Sin embargo, no está siendo usado actualmente.

#   ■ 403 Forbidden (https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Status/403)
#     El cliente no posee los permisos necesarios para cierto contenido, por lo que el servidor está rechazando
#     otorgar una respuesta apropiada.

#   ■ 404 Not Found (https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Status/404)
#     El servidor no pudo encontrar el contenido solicitado. Este código de respuesta es uno de los más
#     famosos dada su alta ocurrencia en la web.


# Errores de servidor
#   ■ 500 Internal Server Error (https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Status/500)
#     El servidor ha encontrado una situación que no sabe cómo manejarla.