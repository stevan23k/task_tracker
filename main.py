from json.decoder import JSONDecodeError
import click
from src.utils import cargar, guardar, generate_id
import datetime


file_path = "data.json"

@click.group
def main():
    pass


# listar tareas
@main.command()
def list():
    tasks = cargar()
    if tasks:
        for i in tasks:
            print(f"{i["id"],i["descripcion"],i["status"], i["createAt"], i["updateAt"]}")
    else:
        print("no se encontraron tareas")


# actualizar usuarios
@main.command()
@click.option("id", "-i")
@click.option("descripcion", "-d", prompt="ingrese la nueva tarea")
def update(id, descripcion):
    tasks = cargar()
    nuevos_datos = {
        "descripcion": f"{descripcion}",
        "updateAt": f"{datetime.datetime.now()}"
    }
    id = int(id)
    for i in tasks:
        if i["id"] == id:
            i.update(nuevos_datos)
            guardar(tasks)
            print(f"la terea con el id: {id} actualizada")
            return
    print(f"usuario con id: {id} no encontrado")

# eliminar tareas
@main.command()
@click.argument("id")
def delete(id):
    tasks = cargar()
    id = int(id)
    for i in tasks:
        if i["id"] == id:
            tasks.remove(i)
            guardar(tasks)
            print(f"tarea con el id: {id} eliminada")



# crear usuarios
@main.command()
@click.option("descripcion", "-d", prompt="ingrese su nombre")
@click.option("status", "-s", default="in-progress")
def add( descripcion, status):
    tasks = cargar()
    nuevo_task ={
        "id": generate_id(tasks),
        "descripcion": f"{descripcion}",
        "status": f"{status}",
        "createAt": f"{datetime.datetime.now()}",
        "updateAt": f"{datetime.datetime.now()}"
    }

    tasks.append(nuevo_task)
    guardar(tasks)
    click.echo(f"tarea creada {nuevo_task['descripcion']}  ")


if __name__ == "__main__":
    main()
