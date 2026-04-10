# Configuración de proyectos utilizando python

## Pre-requisitos

- [Python](https://www.python.org/downloads/)

## Configuración del entorno virtual

Los entornos virtuales son una herramienta que permite crear un espacio aislado para cada proyecto, evitando conflictos entre dependencias y versiones de paquetes. Para configurar un entorno virtual en Python, puedes seguir estos pasos:

- Crea la carpeta de tu proyecto y navega hacía ella

```bash
#Crear carpeta del proyecto
mkdir mi_proyecto
#Navegar hacía la carpeta del proyecto
cd mi proyecto
```

- Para crear el entorno virtual, puedes usar el módulo `venv` que viene incluido con Python. Ejecuta el siguiente comando:

```bash
#Crea un entorno virtual llamado "alias_del_entorno"
#Reemplaza "alias_del_entorno" con el nombre que desees para tu entorno virtual
#Se recomienda usar un nombre descriptivo para el entorno virtual, como ".venv"
python -m venv alias_del_entorno
```

- Una vez creado el entorno virtual, debes activarlo para poder usarlo. El comando para activar el entorno virtual varía según el sistema operativo:

```bash
#Recuerda reemplazar "alias_del_entorno" con el nombre que hayas elegido para tu entorno virtual

#Windows PowerShell
alias_del_entorno\Scripts\Activate.ps1

#Windows bash (WSL o Git Bash)
source alias_del_entorno/Scripts/activate

#Linux/MacOS
source alias_del_entorno/bin/activate
```

- Valida que el entorno virtual esté activo. Deberías ver el nombre del entorno virtual entre paréntesis al inicio de la línea de comandos. Por ejemplo:

```bash
(alias_del_entorno) $
```

- Con el entorno virtual activado, puedes instalar las dependencias necesarias para tu proyecto utilizando `pip`. Por ejemplo:

```bash
#Actualiza pip a la última versión disponible
python -m pip install --upgrade pip
```

- Para desactivar el entorno virtual cuando hayas terminado de trabajar, simplemente ejecuta el siguiente comando:

```bash
deactivate
```

## Instalación de FastAPI

FastAPI es un framework web moderno y de alto rendimiento para construir APIs con Python. Para instalar FastAPI, puedes usar el siguiente comando:

```bash
#Instala FastAPI con las dependencias estándar para desarrollo y producción
#Asegúrate de tener el entorno virtual activado antes de ejecutar este comando
#Recomienda instalar FastAPI con las dependencias estándar para asegurarte de tener todas las herramientas necesarias para el desarrollo y la producción
pip install "fastapi[standard]"
```

## Proyecto como paquete

Para organizar tu proyecto como un paquete de Python, puedes seguir estos pasos:

- Crea una estructura de directorios para tu proyecto. Por ejemplo:

```mi_proyecto/
├── alias_del_entorno/  # Entorno virtual
├── mi_paquete/        # Código fuente del paquete
│   ├── __init__.py    # Archivo de inicialización del paquete  
│   └── modulo.py      # Módulo de ejemplo
├── tests/            # Pruebas del paquete
│   └── test_modulo.py # Prueba de ejemplo
├── README.md         # Documentación del proyecto
└── setup.py          # Archivo de configuración del paquete
```

- El archivo `setup.py` es el archivo de configuración del paquete. Aquí puedes definir la información del paquete, las dependencias y otros detalles. Un ejemplo básico de `setup.py` podría ser:

```python
from setuptools import setup, find_packages

setup(
    name="mi_paquete",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Aquí puedes listar las dependencias de tu paquete
    ],
)
```

**IMPORTANTE**: En python existen archivos como `__init__.py` que indican que el directorio es un paquete de python, por lo tanto, es necesario crear este archivo aunque esté vacío para que el directorio sea reconocido como un paquete.

- Para instalar tu paquete localmente, puedes usar el siguiente comando:

```bash
#Instala el paquete localmente en modo editable
#Esto permite que los cambios en el código fuente se reflejen inmediatamente sin necesidad de reinstalar el paquete
pip install -e .
```

- `pyproject.toml` es un archivo de configuración que se utiliza para definir las dependencias y la configuración del proyecto. Es una alternativa moderna a `setup.py` y se recomienda su uso para proyectos nuevos. Puedes crear un archivo `pyproject.toml` con el siguiente contenido:

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
[project]
name = "mi_paquete"
version = "0.1.0"
dependencies = [
    # Aquí puedes listar las dependencias de tu paquete
]
```

- Para instalar tu paquete utilizando `pyproject.toml`, puedes usar el siguiente comando:

```bash
#Instala el paquete localmente utilizando pyproject.toml
pip install -e .
```
