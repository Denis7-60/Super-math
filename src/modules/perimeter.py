def perimeter_func(arr):
    summ = 0
    for storona in arr:
        summ += storona
    return summ    

arr = list(map(int, input().split()))  # "1 2 3" → [1, 2, 3]
perimeter_func(arr)
