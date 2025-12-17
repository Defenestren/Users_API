# Users API

API REST desarrollada con **FastAPI** como proyecto personal para consolidar fundamentos de backend en Python.

El proyecto implementa un sistema básico de gestión de usuarios con autenticación y operaciones CRUD.

---

## Funcionalidades

- Registro y autenticación básica de usuarios
- Operaciones CRUD sobre usuarios
- Validación de datos con Pydantic
- Control básico de errores
- Documentación automática con Swagger (/docs)

> Proyecto creado con fines formativos. No orientado a producción.

---

## Tecnologías utilizadas

- Python
- FastAPI
- Pydantic
- Uvicorn
- Pytest (tests básicos)

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

---

## Ejecución en local

### 1. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
