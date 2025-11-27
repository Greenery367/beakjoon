
arr = [int(input()) for _ in range(9)]
arr.sort()

a,b = 0,0
for i in range(9):
    for j in range(i+1, 9):
        var = sum(arr)
        if var - (arr[i]+arr[j]) == 100:
            a,b = arr[i],arr[j]
            
for k in arr:
    if k != a and k != b:
        print(k)
