def solution(my_string):
    num_char = str(my_string)
    answer = 0
    
    for i in num_char:
        if i.isdigit():
            answer += int(i)
    return answer