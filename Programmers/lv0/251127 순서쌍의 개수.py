def solution(n):
    answer = 0
    arr = []
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i*j == n:
                arr.append([i,j])
                answer += 1

    return answer