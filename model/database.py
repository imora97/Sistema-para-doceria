import sqlite3
from model.doces_dao import createTableDoces
from model.clientes_dao import createTableClientes
from model.vendas_dao import createTableVendas

def connect():
    conn = sqlite3.connect('database/sistemadoceria.sqlite')
    return conn

def createDB():
    conn = connect()
    cursor = conn.cursor()
    createTableDoces(cursor)
    createTableClientes(cursor)
    createTableVendas(cursor)
    conn.commit()
    conn.close()