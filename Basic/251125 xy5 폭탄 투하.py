arr = [['_'] * 5 for _ in range(4)]
bombs = [list(map(int, input().split())) for __ in range(2)]

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

for i in range(2):
    current_x = bombs[i][1]
    current_y = bombs[i][0]
    for j in range(8):
        nx = current_x + dx[j]
        ny = current_y + dy[j]

        # 배열 인덱스가 유효한 범위 내에 있는지 확인
        if 0 <= ny < 4 and 0 <= nx < 5:
            arr[ny][nx] = '#'

# 결과 출력
for j in arr:
    print(*j)
