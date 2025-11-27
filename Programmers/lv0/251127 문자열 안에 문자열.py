def solution(str1, str2):
    answer = 2  # 기본값은 2
    for i in range(len(str1) - len(str2) + 1):  # 범위 수정
        current = str1[i:i + len(str2)]  # 서브스트링 추출
        if current == str2:
            answer = 1  # str2를 찾으면 1로 설정
            break  # 찾으면 더 이상 비교할 필요 없으므로 break
    return answer
