import model.database as database
from model.clientes import Clientes
import model.

def createTableClientes(cursor):

    cursor.execute("""
    CREATE TABLE "Clientes" (
        "Id"	INTEGER,
        "Nome"	TEXT NOT NULL,
        "Telefone"	NUMERIC NOT NULL,
        PRIMARY KEY("Id" AUTOINCREMENT)
    );
    """)


lista_clientes = []

def adicionar(novo_cliente):
    novo_id = len(lista_clientes)
    novo_cliente.id = novo_id
    lista_clientes.append(novo_cliente)

def editar(cliente):
    for c in range(0, len(lista_clientes)):
        if cliente.id == lista_clientes[c].id:
            lista_clientes[c] = cliente

def excluir_cliente(id):
    for cliente in lista_clientes:
        if cliente.id == id:
            lista_clientes.remove(cliente)