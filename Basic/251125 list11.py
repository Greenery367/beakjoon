arr = []
for i in range(4):
    div = list(map(int, input().split()))
    arr.append(div)

for j in range(4):
    for k in range(4):
        print(arr[3-j][3-k], end=" ")
    print()
