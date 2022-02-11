import model.database as database
import model.doces as doces


def createTableDoces(cursor):

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS "Doces" (
        "Id"	INTEGER,
        "Nome"	TEXT NOT NULL,
        "Peso"	TEXT NOT NULL,
        "Tipo"	TEXT NOT NULL,
        "Valor"	REAL NOT NULL,
        PRIMARY KEY("Id" AUTOINCREMENT)
    );
    """)

def getCatalogo(pesquisa = ''):
    conn = database.connect_database()
    cursor = conn.cursor()
    pesquisa = ""+pesquisa+"%"
    cursor.execute("SELECT * FROM Catalogo c WHERE c.nome LIKE ? ORDER BY c.nome;", [pesquisa])
    lista_doces = []

    for cd in cursor.fetchall():
        id = cd[0]
        nome = cd[1]
        peso = cd[2]
        tipo = cd[3]
        valor = cd[4]
        novocd = doces(id, nome, peso, tipo, valor)
        lista_doces.append(novocd)
    conn.close()
    return lista_doces

def insert(doces):
    try: # tenta executar o código
        conn = database.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Doces (nome, peso, tipo, valor, id) VALUES (?,?,?,?,?);"""
        cursor.execute(sql, [doces.nome, doces.peso, doces.tipo, doces.valor, doces.id])
        conn.commit()
    except Exception as a: # caso dê erro
        print('ERRO!!!')
        print(a)
    finally:
        conn.close()

def update(doces):
    try: # tenta executar o código
        conn = database.connect()
        cursor = conn.cursor()
        sql = """UPDATE Doces SET nome=?, peso=?, tipo=?, valor=? WHERE id=?;"""
        cursor.execute(sql, [doces.nome, doces.peso, doces.tipo, doces.valor, doces.id])
        conn.commit()
    except Exception as a: # caso dê erro
        print(a)
    finally:
        conn.close()

def delete(id):
    try: # tenta executar o código
        conn = database.connect()
        cursor = conn.cursor()
        sql = """DELETE FROM Doces WHERE id=?;"""
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
        sql = """SELECT * FROM Doces ORDER BY upper(nome);"""
        cursor.execute(sql)
        result = cursor.fetchall() # retorna uma lista
        for r in result:
            id = r[0]
            nome = r[1]
            peso = r[2]
            tipo = r[3]
            valor = [4]
            d = doces(id, nome, peso, tipo, valor)
            lista.append(d)
    except Exception as a: # caso dê erro
        print(a)
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