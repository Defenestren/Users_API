# Users API

API REST desarrollada con **FastAPI** como proyecto personal de aprendizaje, orientada a consolidar fundamentos de desarrollo backend en Python.

El proyecto implementa operaciones básicas de gestión de usuarios, validación de datos y tests automáticos, utilizando una base de datos simulada en memoria.

---

## Objetivo del proyecto

Este proyecto ha sido creado con fines **formativos**, con el objetivo de:

- Practicar el diseño de una API REST con FastAPI
- Trabajar con modelos de datos y validación
- Implementar endpoints CRUD
- Añadir tests automáticos básicos con pytest
- Mantener una estructura de proyecto clara y mínima

No está pensado para uso en producción.

---

## Funcionalidades

- Creación de usuarios
- Listado de usuarios
- Obtención de un usuario por ID
- Eliminación de usuarios
- Validación de datos de entrada
- Respuestas HTTP correctas según el resultado de la operación

---

## Tecnologías utilizadas

- Python 3
- FastAPI
- Pydantic
- Uvicorn
- Pytest

---

## Estructura del proyecto

<pre>
Users_API/
├── main.py
├── routers/
│   └── users.py
├── models/
│   └── user.py
├── db/
│   └── fake_db.py
├── tests/
│   └── test_users.py
├── requirements.txt
└── README.md
</pre>

> La persistencia se realiza mediante una base de datos en memoria (`fake_db.py`) con fines formativos.

---

## Ejecución en local

### 1. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

## Tests

---

## Instalación y ejecución

### 2. Clonar el repositorio

```bash
git clone https://github.com/Defenestren/Users_API.git
cd Users_API

pytest

---

### 3. Crear y activar entorno virtual
python -m venv venv


Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

### 4. Instalar dependencias
pip install -r requirements.txt

### 5. Ejecutar la aplicación
uvicorn main:app --reload


La API estará disponible en:

http://127.0.0.1:8000

```bash

---

### Documentación de la API

FastAPI genera documentación automática accesible en:

Swagger UI:

http://127.0.0.1:8000/docs

---

### Tests

El proyecto incluye tests básicos con pytest para validar los endpoints principales.

Ejecutar tests
pytest


Los tests verifican:

Creación de usuarios

Listado de usuarios

Obtención y eliminación de usuarios

Respuestas HTTP correctas
