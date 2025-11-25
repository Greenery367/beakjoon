arr = [0,0,0,0,0]

for _ in range(5):
    div = list(map(int, input().split()))
    arr[_] = div

cnt = 0
max_v = -1
min_v = 99
total = 0
for i in range(5):
    for j in range(5):
        if i == j: total += arr[i][j]
        if arr[i][j] == 2 : cnt += 1
        if arr[i][j] > max_v : max_v = arr[i][j]
        if arr[i][j] < min_v : min_v = arr[i][j]

print(cnt)
print(max_v, min_v)
print(total)