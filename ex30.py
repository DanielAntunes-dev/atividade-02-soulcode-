def reduzir_array(array, funcao_reducao, valor_inicial=None):
    if valor_inicial is None:
        resultado = array[0]
        start_index = 1
    else:
        resultado = valor_inicial
        start_index = 0
    
    for i in range(start_index, len(array)):
        resultado = funcao_reducao(resultado, array[i])
    
    return resultado


numeros = [1, 2, 3, 4, 5]
soma = reduzir_array(numeros, lambda x, y: x + y)
print(soma) 
