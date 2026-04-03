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
