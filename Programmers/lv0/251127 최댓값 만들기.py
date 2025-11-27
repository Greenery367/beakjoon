def solution(numbers):
    answer = 0
    for i in range(len(numbers)):
        for j in range(1, len(numbers)):
            if i != j and numbers[i]*numbers[j] > answer :
                answer = numbers[i] * numbers[j]
    return answer