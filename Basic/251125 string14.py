arr = [2,5,1,6,4,3]

sum_value = 0
max_value = -1
min_value = 99
for i in range(len(arr)):
    sum_value += arr[i]

    if arr[i] > max_value:
        max_value = arr[i]
    if arr[i] < min_value:
        min_value = arr[i]

print(sum_value)
print(max_value - min_value)