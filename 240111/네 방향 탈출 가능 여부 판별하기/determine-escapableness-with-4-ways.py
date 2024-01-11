from collections import deque

N,M = map(int,input().split())

grid = []
for _ in range(N):
    grid.append(list(map(int,input().split())))

n = len(grid)
m = len(grid[0])
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
isT = False
def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m and grid[x][y] == 1

queue = deque([(0, 0)])
visited = set([(0, 0)])

while queue:
    x, y = queue.popleft()
    if (x, y) == (n - 1, m - 1):
        isT = True
        break# Found a path
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny) and (nx, ny) not in visited:
            visited.add((nx, ny))
            queue.append((nx, ny))

if isT:
    print(1)
else:
    print(0)