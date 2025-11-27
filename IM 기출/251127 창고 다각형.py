# 막대기 
N = int(input())

# 막대기 배열
arr = [list(map(int, input().split())) for i in range(N)]
sorted_arr = sorted(arr, key=lambda x:x[0])

#전체 면적
total = 0
biggest = 0
arr = []

# 창고 만들기
for i in range(len(arr)):
    