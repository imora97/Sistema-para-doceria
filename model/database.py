import sqlite3
import model.clientes_dao as clientes
import model.doces_dao as doces
import model.vendas_dao as vendas

def connect():
    conn = sqlite3.connect('database/sistemadoceria.sqlite')
    return conn

def createDB():
    conn = connect()
    cursor = conn.cursor()
    clientes.createTableClientes(cursor)
    doces.createTableDoces(cursor)
    vendas.createTableVendas(cursor)
    conn.commit()
    conn.close()