# 두번째 원소부터 시작하기 때문에
# N-1번 반복
    # 현재 데이터(i)와 이전 데이터 (j)와 비교하면사
    # 나보다 작으면 break
    # 아니면 swap 

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)) :
    for j in range(i, 0, -1) :
        if array[j] > array[j-1] :
            break
        else :
            array[j], array[j-1] = array[j-1], array[j]

print(array) 