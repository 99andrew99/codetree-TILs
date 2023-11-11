import math

num1, num2 = map(int, input().split(" "))
print(f"{math.floor(num1 / num2)}...{math.floor(num1%num2)}")