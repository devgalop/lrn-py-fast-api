# Arquitectura del proyecto

Este proyecto está diseñado como un **monolito**, todas las funcionalidades están contenidas en una sola aplicación. Sin embargo, se ha estructurado de manera modular para facilitar su mantenimiento y escalabilidad. El código está organizado en una **arquitectura de capas verticales basada en features**, lo que permite una separación clara de responsabilidades y una fácil navegación por el código.

## Estructura del proyecto

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
