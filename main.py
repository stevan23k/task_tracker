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
def list_task():
    tasks = cargar()
    if tasks:
        for i in tasks:
            print(f"{i["id"],i["descripcion"],i["status"]}")
    else:
        print("no se encontraron tareas")


# actualizar usuarios
@main.command()
@click.option("id", "-i")
@click.option("nombre", "-n", prompt="ingrese el nuevo nombre")
@click.option("lastName", "-l", prompt="ingrese el nuevo apellido")
def updata_user(id, nombre, lastName):
    clientes = cargar()
    nuevos_datos = {
        "nombre": f"{nombre}",
        "apellido": f"{lastName}"
    }
    id = int(id)
    for i in clientes:
        if i["id"] == id:
            i.update(nuevos_datos)
            guardar(clientes)
            print(f"usuario con el id: {id} actualizado")
            return
    print(f"usuario con id: {id} no encontrado")

@main.command()
@click.argument("id")
def delete_user(id):
    clientes = cargar()
    id = int(id)
    for i in clientes:
        if i["id"] == id:
            clientes.remove(i)
            guardar(clientes)
            print(f"usuario con el id: {id} eliminado")



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
        "updataAt": f"{datetime.datetime.now()}"
    }

    tasks.append(nuevo_task)
    guardar(tasks)
    click.echo(f"tarea creada {nuevo_task['descripcion']}  ")


if __name__ == "__main__":
    main()
