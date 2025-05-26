def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
    
def factorial_normal(n):
    summ = 1
    for i in range(1, n + 1):
        summ *= i
    return summ  
