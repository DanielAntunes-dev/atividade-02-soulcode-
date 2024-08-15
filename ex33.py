def mapear_array(array, funcao_mapeamento):
    return [funcao_mapeamento(x) for x in array]

def quadrado(x):
    return x * x

def maiuscula(s):
    return s.upper()

print(mapear_array([1, 2, 3, 4], quadrado))    
print(mapear_array(['a', 'b', 'c'], maiuscula))