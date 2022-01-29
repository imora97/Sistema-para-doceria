import sqlite3
from model.doces_dao import createTableDoces


def connect():
    conn = sqlite3.connect('database/sistemadoceria.sqlite')
    return conn

def createDB():
    conn = connect()
    cursor = conn.cursor()
    createTableDoces(cursor)
    conn.commit()
    conn.close()