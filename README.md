# Gestión de usuarios - FastAPI

Este proyecto es una API para la gestión de usuarios utilizando FastAPI. Es un repositorio de aprendizaje que incluye funcionalidades básicas para crear, leer, actualizar y eliminar usuarios.

El objetivo principal de este proyecto es proporcionar una base sólida para aprender los conceptos fundamentales de FastAPI y buenas practicas de desarrollo de APIs en Python.

## Tecnologías utilizadas

- Python 3.13
- FastAPI
- Pytest

## Configuración del entorno

Para configurar el entorno de desarrollo puede seguir los pasos establecidos en el archivo [SETUP.md](./docs/SETUP.md).

## Arquitectura del proyecto

Este proyecto sigue una **arquitectura de capas verticales** (Vertical Slice Architecture) **basada en features**. Cada feature representa una funcionalidad específica de la aplicación, lo que facilita la organización y el mantenimiento del código.

```bash
├── src/
│   ├── features/
│   │   ├── user_management/
│   │   │   ├── register_user/
│   │   │   │   ├── register_user_endpoint.py
│   │   │   │   ├── register_user_handler.py
│   │   │   │   ├── register_user_request.py
│   │   │   ├── login_user/
│   │   │   ├── update_user/
│   │   │   ├── shared/
│   │   │   │   ├── init.py
│   │   │   │   ├── user_repository.py
│   │   │   │   ├── user.py
│   ├── infrastructure/
│   ├── main.py
├── tests/
```
