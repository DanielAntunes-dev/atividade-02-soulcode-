def dobrar(x: int) -> int:
  return x * 2

def adicionar_cinco(x: int) -> int:
  return x + 5

def compor(func1, func2):
  return lambda x: func2(func1(x))


nova_func = compor(dobrar, adicionar_cinco)

print(dobrar(5))
print(adicionar_cinco(5))
print(nova_func(10))