arr = [0] * 8

for i in range(8):
    if i<=3:
        arr[i] = 7
    else:
        arr[i] = 15

print(*arr)