arr = [[7,1,3,5], [9,5,9,1], [1,3,1,5], [3,5,9,9]]
num = 1

for i in range(4):
    if i == 3 and num == 4 :
        num = 0
    print(arr[i][num])
    num += 1
