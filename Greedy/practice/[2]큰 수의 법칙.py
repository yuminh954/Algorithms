N, M, K = map(int, input().split())
list = list(map(int, input().split()))
list.sort(reverse=True)

first = list[0]
second = list[1]
result = 0
cnt = 0
m = 0

while True :
    if cnt == K :
        result += second
        cnt = 0
    else :
        result += first
        cnt += 1
        
    m += 1
    if m == M :
        break

print(result)