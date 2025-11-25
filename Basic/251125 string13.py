arr = [0] * 8
a,b = map(int, input().split())

for i in range(8):
    if i <= 2:
        arr[i] = a
    elif i <= 4:
        arr[i] = b
    else:
        arr[i] = a+b

print(*arr)