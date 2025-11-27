def solution(my_string):
    answer = ''
    arr = ['a','e','i','o','u']
    
    for i in my_string:
        if arr.count(i) == 0:
            answer += i
    
    return answer