def solution(numbers):
    # numbers에서 가장 큰 두 수와 가장 작은 두 수를 구합니다.
    numbers.sort()  # 리스트를 오름차순으로 정렬
    
    # 가장 큰 두 수의 곱과 가장 작은 두 수의 곱을 비교합니다.
    max_product = numbers[0] * numbers[1]  # 가장 작은 두 수의 곱
    min_product = numbers[-1] * numbers[-2]  # 가장 큰 두 수의 곱
    
    # 두 결과 중 더 큰 값을 반환
    return max(max_product, min_product)
