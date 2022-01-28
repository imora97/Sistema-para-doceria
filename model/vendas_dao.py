

lista_vendas = []

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
            lista_vendas.remove(venda)