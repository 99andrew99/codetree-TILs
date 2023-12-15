def printSomthing(n):
    print('1' * n)

a,b = map(int, input().split(" "))
for i in range(a):
    printSomthing(b)