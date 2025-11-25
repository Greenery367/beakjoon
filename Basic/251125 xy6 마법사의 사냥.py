N = int(input())
field = [[0] for _ in range(N)]

# field
for n in range(N):
    arr = list(map(int, input().split()))
    field[n] = arr

# 마법의 위력
k = int(input())

# dxdy 배열
dx = [-1,1,-1,1]
dy = [-1,-1,1,1]

# 현재 위치
x,y = int(k//2)+1, k//2+1

# 총합
total = 0

# 마법의 위력만큼
for i in range(k):
    # 네 방향으로
    for j in range(4):
        nx = x + (dx[j] * k)
        ny = y + (dy[j] * k)
        if 0 <= nx < 5 and 0 <= ny < 5:
            print(ny,nx)
            total += field[ny][nx]

print(total)

