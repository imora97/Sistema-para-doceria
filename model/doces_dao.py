

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


lista_doces = []

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
            lista_doces.remove(doce)