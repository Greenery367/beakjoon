# 세로, 가로
N, M = map(int, input().split())
# 화력
K = int(input())

# 배경
field = []

# 필드 입력 받기
for n in range(N):
    field.append(list(input().strip()))

# 폭탄 위치 알아내기
bomb_list = []

for i in range(N):
    for j in range(M):
        if field[i][j] == '@':
            bomb_list.append([i, j])

# 탐색 방향 (상, 좌, 우, 하)
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 폭탄 주변에 영향을 미치는 영역을 '%'
for k in range(len(bomb_list)):
    current_bomb = bomb_list[k]
    field[current_bomb[0]][current_bomb[1]] = '%'  # 현재 폭탄 위치를 '%'

    # 폭탄의 주변을 K번까지 영향을 미친다
    for f in range(1, K + 1):  # f는 폭탄의 영향 범위 (1부터 K까지)
        for e in range(4):  # 4방향 탐색 (상, 좌, 우, 하)
            nx = current_bomb[1] + (dx[e] * f)
            ny = current_bomb[0] + (dy[e] * f)

            # 범위 안에 있고, 벽이 아니면 영향을 미침
            if 0 <= nx < M and 0 <= ny < N and field[ny][nx] != '#':
                field[ny][nx] = '%'

# 결과 출력
for row in field:
    print(''.join(row))
