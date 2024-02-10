# 숫자의 개수를 카운트 하고, 그 만큼 출력하는 알고리즘
# 1. 0부터 array 내 가장 큰 숫자까지의 count_list를 생성
# 2. array 반복하며 해당 숫자 index에 += 1

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count_list = [0] * (max(array) + 1)

for i in range(len(array)) :
    count_list[array[i]] += 1

for i in range(len(count_list)) :
    for j in range(count_list[i]) :
        print(i, end=" ")
        