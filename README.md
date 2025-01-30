<div align="center">

# task tracker

task tracker es un sistema para seguimiento de tareas

### como instalar

```
git clone https://github.com/stevan23k/task_tracker.git

cd task-tracker

pip install .

C:\Users\[user]\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts

Presiona Win + R, escribe sysdm.cpl y presiona Enter.

Ve a la pestaña Opciones avanzadas y haz clic en Variables de entorno.

En la sección Variables del sistema, selecciona Path y haz clic en Editar.

Haz clic en Nuevo, pega la ruta copiada y guarda los cambios.
```
### como usar
###### agrear tareas

``
task add -d "tarea de ejemplo"
``
###### actualizar tareas

``
task update 1 -> id de la tarea a editar
``
###### eliminar tarea

``
task delete 1 -> id de la tarea a eliminar
``
###### listar tareas

``
task list
``
###### cambiar estado de la tarea
```
task todo 1 -> id de la tarea a modificar
task complete 1 -> id de la tarea a modificar

```

