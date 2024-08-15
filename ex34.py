def ordenar(array, funcao_comparacao):
    return sorted(array, key=funcao_comparacao)

pessoas = [
    {'nome': 'Daniel', 'idade': 37},
    {'nome': 'Gabriel', 'idade': 34},
    {'nome': 'Caio', 'idade': 28}
]

def por_idade(pessoa):
    return pessoa['idade']

print(ordenar(pessoas, por_idade))

