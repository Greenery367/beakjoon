arr = [
    [1,2,1,3,1],
    [2,2,2,2,2],
    [1,0,1,0,1],
    [3,1,2,1,3]
]

dx = [-1,0,1,1]
dy = [0,1,0,1]

x,y = map(int, input().split())
max_v = 0

for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    if max_v < arr[ny][nx]:
        max_v = arr[ny][nx]

print(max_v)
