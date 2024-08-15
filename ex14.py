def contagem_regressiva(numero):
    if numero < 0:
        return
    print(numero)
    contagem_regressiva(numero - 1)

# Exemplo de uso:
contagem_regressiva(5)
