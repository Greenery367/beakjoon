arr = [
    [1,2,1,3,1],
    [2,2,2,2,2],
    [1,0,1,0,1],
    [3,1,2,1,3]
]

total = 0
dy = [-1,0,0,1]
dx = [0,-1,1,0]

for i in range(4):
    y = 1
    x = 2
    ny = y+dy[i]
    nx = x+dx[i]

    total += arr[ny][nx]

print(total)