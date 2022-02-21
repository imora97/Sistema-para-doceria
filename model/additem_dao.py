import model.database as database
import model.additem_dao as additem


def createTableAddItem(cursor):

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS "AddItem" (
	"Id"	INTEGER UNIQUE,
	"Nome"	TEXT NOT NULL,
	PRIMARY KEY("Id" AUTOINCREMENT)
    );
    """)

def insert(additem):
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO AddItem (nome, id) VALUES (?,?);"""
        cursor.execute(sql, [additem.nome, additem.id])
        conn.commit()
    except Exception as a:
        print('\033[1;34;41mERRO!!!\033[m')
        print(a)
    finally:
        conn.close()

def update(additem):
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """UPDATE AddItem SET nome=? WHERE id=?;"""
        cursor.execute(sql, [additem.nome, additem.id])
        conn.commit()
    except Exception as a:
        print(a)
    finally:
        conn.close()

def delete(id):
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """DELETE FROM AddItem WHERE id=?;"""
        cursor.execute(sql, [id])
        conn.commit()
    except Exception as a:
        print(a)
    finally:
        conn.close()

def selectAll():
    lista = []
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM AddItem ORDER BY upper(nome);"""
        cursor.execute(sql)
        result = cursor.fetchall()
        for r in result:
            id = r[0]
            nome = r[1]
            ai = additem(id, nome)
            lista.append(ai)
    except Exception as a:
        print(a)
    finally:
        conn.close()