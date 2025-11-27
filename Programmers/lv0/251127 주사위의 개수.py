def solution(box, n):
    answer = 0
    width = box[0] // n
    height = box[1] // n
    meter = box[2] // n
    answer = meter * width * height
    return answer