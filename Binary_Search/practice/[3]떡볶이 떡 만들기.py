# 떡의 길이가 매우 길었다면 순차 탐색으로 푸는 것은 부적절하다.
# 적절한 값을 찾을 때 이진 탐색으로 푸는 것이 적절하다.

# --------- 순차 탐색 --------------
"""
N, M = map(int, input().split())
data_list = list(map(int, input().split()))
data_list.sort()

data_len = len(data_list)
H = max(data_list)
for i in range(H, 0, -1) :
    total_len = 0
    for j in range(0, data_len) :
        len = data_list[j] - i
        if len > 0 :
            total_len += len
    if total_len >= M :
        result = i
        break
print(result)
"""

# --------- 이진 탐색 --------------
N, M = map(int, input().split())
data_list = list(map(int, input().split()))

start = 0
end = max(data_list)

result = 0
while start <= end :
    total = 0
    mid = (start + end) // 2
    for x in data_list :
        if x > mid :
            total += x - mid
    if total < M :
        end = mid - 1
    else :
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기서 result에 기록하며 갱신
        start = mid + 1

print(result)