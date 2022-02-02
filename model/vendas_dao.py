import model.database as database
import model.vendas as vendas


def createTableVendas(cursor):

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS "Vendas" (
        "Id"	INTEGER,
        "Item"	TEXT NOT NULL,
        "Quantidade"	NUMERIC NOT NULL,
        "Tipo"	TEXT NOT NULL,
        "Valor"	NUMERIC NOT NULL,
        PRIMARY KEY("Id" AUTOINCREMENT)
    );
    """)

def insert(vendas):
    try: # tenta executar o código
        conn = database.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Vendas (item, quantidade, tipo, valor, id) VALUES (?,?,?,?,?);"""
        cursor.execute(sql, [vendas.item, vendas.quantidade, vendas.tipo, vendas.valor, vendas.id])
        conn.commit()
    except Exception as a: # caso dê erro
        print('ERRO!!!')
        print(a)
    finally:
        conn.close()

def update(vendas):
    try: # tenta executar o código
        conn = database.connect()
        cursor = conn.cursor()
        sql = """UPDATE Vendas SET item=?, quantidade=?, tipo=?, valor=? WHERE id=?;"""
        cursor.execute(sql, [vendas.item, vendas.quantidade, vendas.tipo, vendas.valor, vendas.id])
        conn.commit()
    except Exception as a: # caso dê erro
        print(a)
    finally:
        conn.close()

def delete(id):
    try: # tenta executar o código
        conn = database.connect()
        cursor = conn.cursor()
        sql = """DELETE FROM Vendas WHERE id=?;"""
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
        sql = """SELECT * FROM Vendas ORDER BY upper(nome);"""
        cursor.execute(sql)
        result = cursor.fetchall() # retorna uma lista clientes
        for r in result:
            id = r[0]
            item = r[1]
            quantidade = r[2]
            tipo = r[3]
            valor = [4]
            v = vendas(id, item, quantidade, tipo, valor)
            lista.append(v)
    except Exception as a: # caso dê erro
        print(a)
    finally:
        conn.close()
    return lista


"""lista_vendas = []

def adicionar(nova_venda):
    novo_id = len(lista_vendas)
    nova_venda.id = novo_id
    lista_vendas.append(nova_venda)

def editar(venda):
    for v in range(0, len(lista_vendas)):
        if venda.id == lista_vendas[v].id:
            lista_vendas[v] = venda

def excluir_venda(id):
    for venda in lista_vendas:
        if venda.id == id:
            lista_vendas.remove(venda)"""