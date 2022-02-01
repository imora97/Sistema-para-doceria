import model.database as database
from model.doces import Doces

def createTableDoces(cursor):

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS "Doces" (
        "Id"	INTEGER,
        "Nome"	TEXT NOT NULL,
        "Peso"	NUMERIC NOT NULL,
        "Tipo"	TEXT NOT NULL,
        "Valor"	NUMERIC NOT NULL,
        PRIMARY KEY("Id")
    );
    """)

def insert(Doces):
    try: # tenta executar o código
        conn = database.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Doces (nome, peso, tipo, valor, id) VALUES (?,?,?,?,?);"""
        cursor.execute(sql, [Doces.nome, Doces.peso, Doces.tipo, Doces.valor, Doces.id])
        conn.commit()
    except: # caso dê erro
        print('ERRO!!!')
    finally:
        conn.close()

def update(Doces):
    try: # tenta executar o código
        conn = database.connect()
        cursor = conn.cursor()
        sql = """UPDATE Doces SET nome=?, peso=?, tipo=?, valor=? WHERE id=?;"""
        cursor.execute(sql, [Doces.nome, Doces.peso, Doces.tipo, Doces.valor, Doces.id])
        conn.commit()
    except: # caso dê erro
        print('ERRO!!!')
    finally:
        conn.close()

def delete(id):
    try: # tenta executar o código
        conn = database.connect()
        cursor = conn.cursor()
        sql = """DELETE FROM Doces WHERE id=?;"""
        cursor.execute(sql, [id])
        conn.commit()
    except: # caso dê erro
        print('ERRO!!!')
    finally:
        conn.close()

def selectAll():
    lista = []
    try: # tenta executar o código
        conn = database.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM Doces ORDER BY upper(nome);"""
        cursor.execute(sql)
        result = cursor.fetchall() # retorna uma lista clientes
        for r in result:
            id = r[0]
            nome = r[1]
            peso = r[2]
            tipo = r[3]
            valor = [4]
            d = Doces(id, nome, peso, tipo, valor)
            lista.append(d)
    except: # caso dê erro
        print('ERRO!!!')
    finally:
        conn.close()
    return lista


"""lista_doces = []

def adicionar(novo_doce):
    novo_id = len(lista_doces)
    novo_doce.id = novo_id
    lista_doces.append(novo_doce)

def pegar_doce(id):       ##### 'pegar doce' para quê???
    for doce in lista_doces:
        if doce.id == id:
            return doce
    return None

def editar(doce):
    for d in range(0, len(lista_doces)):
        if doce.id == lista_doces[d].id:
            lista_doces[d] = doce
        
def excluir_doce(id):
    for doce in lista_doces:
        if doce.id == id:
            lista_doces.remove(doce)"""