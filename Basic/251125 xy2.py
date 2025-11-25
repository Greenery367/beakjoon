arr = [
    [1,2,1,3,1],
    [2,2,2,2,2],
    [1,0,1,0,1],
    [3,1,2,1,3]
]

dx = [-1,0,0,1]
dy = [0,-1,1,0]

x = 1
y = 0

total = 0

for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]

    if nx >= 0  and ny >= 0:
        total += arr[ny][nx]

print(total)