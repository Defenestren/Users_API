# Users API

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-green)
![Tests](https://img.shields.io/badge/tests-pytest-success)
![Status](https://img.shields.io/badge/status-learning_project-informational)

API REST desarrollada con **Python y FastAPI** como proyecto personal para consolidar fundamentos de desarrollo backend.

Proyecto centrado en la gestión de usuarios, con operaciones CRUD, validación de datos y tests automatizados, aplicando una estructura clara y buenas prácticas básicas de diseño de APIs.

---

## 🚀 Funcionalidades

- Creación de usuarios
- Listado de usuarios
- Obtención de usuario por ID
- Eliminación de usuarios
- Validación de datos con Pydantic
- Persistencia en memoria (fake database)
- Tests automatizados con pytest
- Documentación automática con Swagger UI

---

## 🗂️ Estructura del proyecto

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

## 🛠️ Tecnologías utilizadas

- **Python**
- **FastAPI**
- **Pydantic**
- **Pytest**
- **Uvicorn**

---

## ▶️ Ejecución en local

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/Marcial-Godes/Users_API.git
cd Users_API
```

### 2️⃣ Crear y activar entorno virtual
```bash
python -m venv venv
```
Windows
```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4️⃣ Ejecutar la API

```bash
uvicorn main:app --reload
```

La API estará disponible en:

```bash
http://127.0.0.1:8000
```

Swagger UI:

```bash
http://127.0.0.1:8000/docs
```

---

🧪 Tests

Tests implementados con pytest.

Ejecutar tests:

```bash
pytest
```

Casos cubiertos:

- Creación de usuarios

- Listado de usuarios

- Eliminación de usuarios

- Respuestas HTTP correctas

---

### 🎯 Objetivo del proyecto

Proyecto con fines formativos, orientado a practicar:

Diseño de APIs REST

Organización de proyectos backend

Validación de datos

Testing automatizado básico

Uso de FastAPI en un contexto realista

No orientado a producción.
