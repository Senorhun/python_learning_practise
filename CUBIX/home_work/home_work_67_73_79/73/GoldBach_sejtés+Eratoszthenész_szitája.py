from datetime import datetime
from unittest import result

def eratoszthenesz_szitaja(max_n):
    is_prim = [True] * (max_n + 1)
    is_prim[0] = is_prim[1] = False
    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prim[i]:
            for j in range(i * i, max_n + 1, i):
                is_prim[j] = False
    return {i for i in range(max_n + 1) if is_prim[i]}

def goldbach_finder(prims, n):
    for p in prims:
        if n - p in prims:
            return p, n - p
    return None

def max_goldbach(n):
    prims = eratoszthenesz_szitaja(n)
    result = (0, 0, 0)
    for i in range(4, n, 2):
        final_result = goldbach_finder(prims, i)
        if final_result and final_result[0] > result[1]:
            result = (i, final_result[0], final_result[1])
    return result

before = datetime.now()
print(max_goldbach(10_000_000))
print('Futási idő:', datetime.now() - before)