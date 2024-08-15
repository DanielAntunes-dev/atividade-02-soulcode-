def fatorial(n: int) -> int:
  if n == 0:
    return 1
  else:
    return n * fatorial(n - 1) 
  
# USO
print(fatorial(5))