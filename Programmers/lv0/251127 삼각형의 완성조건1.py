def solution(sides):
    sides.sort()
    
    longest = sides[2]
    others = sides[:2]
    answer = 0
    
    if longest >= sum(others) : answer = 2
    else : answer = 1
    
    return answer