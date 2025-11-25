arr = [
    [1,2,1,3,1],
    [2,2,2,2,2],
    [1,0,1,0,1],
    [3,1,2,1,3]
]

x,y = map(int, input().split())

dx = [-1,-1,1,1]
dy = [-1,1,-1,1]

total = arr[y][x]

for i in range(4):
    nx = dx[i] + x
    ny = dy[i] + y

    total *= arr[ny][nx]

print(total)