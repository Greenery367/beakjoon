def solution(my_string):
    answer = ''
    arr = []
    
    # 주어진 문자열을 소문자로 변환
    my_string = my_string.lower()
    
    # 순서대로 숫자 변환
    for i in my_string:
        arr.append(ord(i))
    
    # 정렬
    arr.sort()
    
    for j in arr:
        answer += chr(j)
        
    return answer