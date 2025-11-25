n = int(input())
now_value = n
for i in range(n):
    for j in range(3):
        print(now_value, end=" ")
        now_value += 1
    print()
    now_value -= 2