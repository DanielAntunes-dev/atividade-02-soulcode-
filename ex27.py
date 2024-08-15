def memoria_fatorial(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return 1
    
    memo[n] = n * memoria_fatorial(n - 1, memo)
    return memo[n]

print(memoria_fatorial(5))

