N = int(input())
list = input().split()
list.sort()

cnt = 0
result = 0

for i in range(N) :
    cnt += 1
    capacity = int(list[i])
    if cnt == capacity :
        cnt = 0
        result += 1

print(result)   