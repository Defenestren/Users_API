# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=20480

### Users DB API ###
from fastapi import APIRouter
from db.client import fake_db
from db.models.user import User

router = APIRouter()

@router.get("/users")
def get_users():
    return fake_db["users"]

@router.post("/users")
def create_user(user: User):
    fake_db["users"].append(user)
    return user






@router.get("/users")
def get_users():
    return fake_db["users"]

@router.post("/users")
def create_user(user: User):
    fake_db["users"].append(user)
    return user


"""
router = APIRouter(
    prefix="/userdb",
    tags=["userdb"],
    responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}}
)


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


@router.get("/", response_model=list[User])
async def users():
    return users_schema(db_client.users.find())
#   Thunder client:
#       Url local (GET): http://127.0.0.1:8000/userdb
#           Mensaje: La lista de usuarios en MongoDB


# Path
@router.get("/{id}")
async def user(id: str):
    return search_user("_id", ObjectId(id))
#   Thunder client:
#       Url local (GET): http://127.0.0.1:8000/userdb/68b0174667180ac48cba2194
#           Mensaje: {"id": "68b0174667180ac48cba2194", "username": "LaCheni", "email": "jatset82@gmail.com"}


# Query
@router.get("/query/{id}")
async def user(id: str):return search_user("_id", ObjectId(id))
#   Thunder client:
#       Url local (GET): http://127.0.0.1:8000/userdb/query/68b0174667180ac48cba2194
#           Mensaje: {"id": "68b0174667180ac48cba2194", "username": "LaCheni", "email": "jatset82@gmail.com"}

#       Url local (GET): http://127.0.0.1:8000/userdb/query/68b0174667180ac48cba2195
#           Mensaje: {"error": "No se ha encontrado el usuario"}


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
    if type(search_user("email", user.email)) == User:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")

    user_dict = dict(user)
    del user_dict["id"]

    id = db_client.users.insert_one(user_dict).inserted_id

    new_user = user_schema(db_client.users.find_one({"_id": id}))

    return User(**new_user)
#   Thunder client:
#       Url local (POST): http://127.0.0.1:8000/userdb
#           Body > JSON > JSON Content:
#               {"username": "Defenestren","email": "mazinguer769@gmail.com"}
#               Mensaje: {"id": "68b044e733a78e561fea46f1", "username": "Defenestren", "email": "mazinguer769@gmail.com"}


@router.put("/", response_model=User)
async def user(user: User):

    user_dict = dict(user)
    del user_dict["id"]

    try:
        db_client.users.find_one_and_replace(
            {"_id": ObjectId(user.id)}, user_dict)
    except:
        return {"error": "No se ha actualizado el usuario"}

    return search_user("_id", ObjectId(user.id))
#   Thunder client:
#       Url local (PUT): http://127.0.0.1:8000/userdb
#           Body > JSON > JSON Content:
#               Mensaje: (Actualiza el usuario)
#                        {"id": "68b02be95e8d51588f7e826b", "username": "BigRock2", "email": "MarcialGodes@gmail.com"}


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user(id: str):

    found = db_client.local.users.find_one_and_delete({"_id": ObjectId(id)})


    if not found:
        raise HTTPException(status_code=404,detail="error: No se ha eliminado el usuario.")
#   Thunder client:
#       Url local (DELETE): http://127.0.0.1:8000/userdb/68b0155e67180ac48cba2193
#           Mensaje: (Nada) Status: 204 No Content
#       Url local (GET): http://127.0.0.1:8000/userdb/68b0155e67180ac48cba2193
#           Mensaje: {"error": "No se ha encontrado el usuario"}


def search_user(field: str, key):

    try:
        user = db_client.local.users.find_one({field:key})
        return User(**user_schema(user))
    
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
"""