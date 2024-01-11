from itertools import product
from collections import deque

N = int(input())
combs = product(['1','2','3','4'], repeat = N)
count = 0

for comb in combs:
    queue = deque(comb)
    isB = True
    while queue:
        if queue[0] == "1":
            queue.popleft()
        elif queue[0] == "2":
            if len(queue) < 2:
                isB = False
                break
            else:
                num1 = queue.popleft()
                num2 = queue.popleft()
                if num1 == num2 == "2":
                    continue
                else:
                    isB = False
                    break
        elif queue[0] == "3":
            if len(queue) < 3:
                isB = False
                break
            else:
                num1 = queue.popleft()
                num2 = queue.popleft()
                num3 = queue.popleft()
                if num1 == num2 == num3 == "3":
                    continue
                else:
                    isB = False
                    break
        elif queue[0] == "4":
            if len(queue) < 4:
                isB = False
                break
            else:
                num1 = queue.popleft()
                num2 = queue.popleft()
                num3 = queue.popleft()
                num4 = queue.popleft()
                if num1 == num2 == num3 == num4 == "4":
                    continue
                else:
                    isB = False
                    break

    if isB:
        count +=1
print(count)