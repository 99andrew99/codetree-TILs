from itertools import product

N, K = map(int, input().split())
arr = [num + 1 for num in range(N)]

combs = product(arr, repeat = K)

for comb in combs:
    print(" ".join(map(str, comb)))