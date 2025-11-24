arr = [12, 3, 9, 1, 15, 7]

def bubbleSort(a,N):
    for i in range(N):
        for j in range(N-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    print(a)

bubbleSort(arr, len(arr))