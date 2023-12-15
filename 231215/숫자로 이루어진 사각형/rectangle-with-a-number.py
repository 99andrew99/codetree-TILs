n = int(input())

cur = 1

temp = []

for i in range(n):
    for j in range(n):
        temp.append(cur)
        if cur == 9:
            cur = 1
        else:
            cur += 1
    print(" ".join(map(str, temp)))
    temp = []