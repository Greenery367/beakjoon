# 테스트 케이스 개수
t = int(input())

for _ in range(1,t+1):
    w = int(input())
    boxes = list(map(int, input().split()))

    max_v = 0

    for i in range(len(boxes)):
        current_values = 0
        for j in range(len(boxes)-i):
            if boxes[i] > boxes[j]:
                current_values += 1
        if current_values > max_v :
            print(current_values)
            max_v = current_values
    print(f"#{_} {max_v}")

