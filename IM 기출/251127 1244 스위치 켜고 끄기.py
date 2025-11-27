switch_n = int(input())
arr = list(map(int, input().split()))
std_num = int(input())
std_arr = []
for _ in range(std_num):
    std_arr.append(list(map(int, input().split())))
    
for t in std_arr:
    # 1. 남학생
    if t[0] == 1:
        num = t[1]
        # 1-1. 배열을 순회하면서
        for i in range(len(arr)+1):
            # 1-2. x의 배수라면 전구 on/off
            if i % num == 0 and i-1 > -1:            
                arr[i-1] = (arr[i-1] + 1) % 2
    
    # 2. 여학생
    else:
        # 현재 위치
        num = t[1]-1
        # start, end
        stored = [0,0]
        # 대칭 구간 찾기
        for j in range(1,len(arr)+1):
            if num-j == 0 or num-j == len(arr) or arr[num-j] != arr[num+j]:
                stored = [num-j, num+j]
                break
        # 대칭 구간 - onoff 뒤집기
        for k in range(stored[0], stored[1]+1):
            arr[k] = (arr[k]+1) % 2
    
                
            
print(*arr)