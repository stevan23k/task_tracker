from json.decoder import JSONDecodeError
import click
import json
import os


file_path = "data.json"

@click.group
def main():
    pass

@main.command()
def list_users():
    print("lista de usuarios")

@main.command()
def updata_user():
    print("actualizando usuarios")

@main.command()
def delete_user():
    print("eliminando usuarios")

# crear usuarios

def generate_id(clientes):
    return len(clientes) + 1 if clientes else 1

def cargar():
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                data = json.load(file)
                if isinstance(data, list):
                    return data
            except json.JSONDecodeError:
                pass
    return []

def guardar(clientes):
    with open(file_path, "w") as file:
        json.dump(clientes,file, indent=4)


@main.command()
@click.option("name", "-n", prompt="ingrese su nombre")
@click.option("lastName", "-l", default="", prompt="ingrese su apellido")
@click.option("active", "-a", default=True)
@click.option("password", "-p", hide_input=True, prompt="ingrese su contraseña" )

def create_user( name, lastName, active, password):
    clientes = cargar()
    nuevo_cliente ={
        "id": generate_id(clientes),
        "nombre": f"{name}",
        "apellido": f"{lastName}",
        "activate": f"{active}",
        "password": f"{password}"
    }

    clientes.append(nuevo_cliente)
    guardar(clientes)
    click.echo(f"usuario creado")


if __name__ == "__main__":
    main()
