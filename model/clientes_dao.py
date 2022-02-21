import model.database as database
import model.clientes_dao as clientes


def createTableClientes(cursor):

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS "Clientes" (
	"Id"	INTEGER UNIQUE,
	"Nome"	TEXT NOT NULL,
	"Telefone"	TEXT NOT NULL,
	PRIMARY KEY("Id" AUTOINCREMENT)
    );
    """)

def insert(clientes):
    try: # tenta executar o código
        conn = database.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Clientes (nome, telefone, id) VALUES (?,?,?);"""
        cursor.execute(sql, [clientes.nome, clientes.telefone, clientes.id])
        conn.commit()
    except Exception as a: # caso dê erro
        print('\033[1;34;41mERRO!!!\033[m')
        print(a)
    finally:
        conn.close()

def update(clientes):
    try: # tenta executar o código
        conn = database.connect()
        cursor = conn.cursor()
        sql = """UPDATE Clientes SET nome=?, telefone=? WHERE id=?;"""
        cursor.execute(sql, [clientes.nome, clientes.telefone, clientes.id])
        conn.commit()
    except Exception as a: # caso dê erro
        print(a)
    finally:
        conn.close()

def delete(id):
    try: # tenta executar o código
        conn = database.connect()
        cursor = conn.cursor()
        sql = """DELETE FROM Clientes WHERE id=?;"""
        cursor.execute(sql, [id])
        conn.commit()
    except Exception as a: # caso dê erro
        print(a)
    finally:
        conn.close()

def selectAll():
    lista = []
    try: # tenta executar o código
        conn = database.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM CLIENTES ORDER BY upper(nome);"""
        cursor.execute(sql)
        result = cursor.fetchall() # retorna uma lista clientes
        for r in result:
            id = r[0]
            nome = r[1]
            telefone = r[2]
            c = clientes(id, nome, telefone)
            lista.append(c)
    except Exception as a: # caso dê erro
        print(a)
    finally:
        conn.close()
    return lista


"""lista_clientes = []

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
            lista_clientes.remove(cliente)"""