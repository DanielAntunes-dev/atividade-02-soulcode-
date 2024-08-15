def calculadora_simples(operacao):
  return lambda *args: operacao(*args)


def soma(*args):
    return sum(args)

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b if b != 0 else "Erro: Divisão por zero"


operacao_soma = calculadora_simples(soma)
operacao_subtracao = calculadora_simples(subtracao)
operacao_multiplicacao = calculadora_simples(multiplicacao)
operacao_divisao = calculadora_simples(divisao)

print(operacao_soma(10,5))
print(operacao_subtracao(10,5))
print(operacao_multiplicacao(10,5))
print(operacao_divisao(10,5))
