```md
![pytest](https://img.shields.io/badge/tests-passing-brightgreen)

# Users API

API REST simple para la gestión de usuarios desarrollada con **Python y FastAPI**, creada como proyecto personal con fines formativos para consolidar fundamentos de backend.

---

## Descripción

El proyecto implementa una API REST que permite registrar usuarios y realizar operaciones CRUD básicas.  
Está orientado a la práctica de conceptos clave de desarrollo backend: diseño de endpoints, validación de datos, estructura de proyecto y manejo básico de estado.

> Proyecto formativo. No orientado a producción.

---

## Funcionalidades

- Registro de usuarios
- Operaciones CRUD sobre usuarios
- Validación de datos con Pydantic
- Control básico de errores
- Documentación automática con Swagger (`/docs`)

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

> La persistencia se realiza mediante una base de datos en memoria (`fake_db.py`) con fines formativos.

---

## Ejecución en local

### 1. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

## Tests

El proyecto incluye tests básicos con pytest.

```bash
pytest

