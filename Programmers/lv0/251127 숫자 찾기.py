def solution(num, k):
    answer = -1
    nchr = str(num)
    
    for i in range(len(nchr)):
        current = (int(nchr[i]))
        if current == k:
            answer = i+1
            break
    
    return answer