def solution(numbers):
    biggest = 0
    for i in range(len(numbers)):
        current = numbers[i]
        for j in range(i+1, len(numbers)):
            current2 = numbers[j]
            if current == 0 or current2 == 0 : continue
            if biggest < current * current2 : biggest = current * current2
    answer = biggest
    return answer