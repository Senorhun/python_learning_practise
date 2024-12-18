N = 120
prim_e = (N+1) * [True]
prim_e[0:1] = 2 * [False]
for i in range(2, int(N ** 0.5) + 1):
    for j in range(2*i, N+1, i):
        prim_e[j] = False

primes = []
for i in range(N+1):
    if prim_e[i]:
        primes.append(i)
print(primes)