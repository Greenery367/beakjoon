def solution(array):
    answer = []
    for i in range(len(array)):
        if array[i] > answer[0]:
            print(answer[0],answer[1])
            answer[0] = array[i]
            answer[1] = i
    return answer