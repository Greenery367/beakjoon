def solution(slice, n):
    flag = True
    answer = 1
    
    while flag:
        if slice*answer >= n :
            flag = False
        else:
            answer += 1
    
    return answer