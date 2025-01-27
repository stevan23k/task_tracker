import click
import json


data = {}
data["clientes"]= []

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


@main.command()
@click.option("name", "-n", prompt="ingrese su nombre")
@click.option("lastName", "-l", default="", prompt="ingrese su apellido")
@click.option("active", "-a", default=True)
@click.option("password", "-p", hide_input=True, prompt="ingrese su contraseña" )
def create_user(name, lastName, active, password):
    data["clientes"].append({
        "nombre": f"{name}",
        "apellido": f"{lastName}",
        "activate": f"{active}",
        "password": f"{password}"
    })
    print(f"se creo el usuario de {name}")
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    main()