from collections import deque

N,M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int,input().split())))

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def isV(x,y):
    return 0 <= x < N and 0 <= y < M and grid[x][y] == 1

queue = deque([(0,0)])
visited = set([(0,0)])
isT = False
while queue:
    x,y = queue.popleft()
    if (x,y) == (N-1, M-1):
        isT = True
        break
    for dx, dy in directions:
        nx,ny = x + dx, y + dy
        if isV(nx,ny) and (nx, ny) not in visited:
            visited.add((nx,ny))
            queue.append((nx,ny))

if isT:
    print(1)
else:
    print(0)