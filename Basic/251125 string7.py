n = int(input())

if n % 2 == 0 :
    for i in range(6) :
        print(n, end=" ")
        n += 2
else:
    for j in range(11) :
        print(n, end=" ")
        n += 3