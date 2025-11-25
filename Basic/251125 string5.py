a,b = map(int, input().split())

if a>b :
    for i in range(a-b+1):
        print(b+i, end=" ")
else:
    for j in range(b-a+1):
        print(a+j, end=" ")