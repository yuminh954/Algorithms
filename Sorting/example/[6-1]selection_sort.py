# array 모든 값 반복
    # 초기 min_idx는 현재 index
    # 현재 idx ~ array 끝 idx 반복하면서 
        # min_idx update
    # array에서 현재 idx랑 min이랑 swap

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)) :
    min_idx = i
    for j in range(i + 1, len(array)) :
        if array[min_idx] > array[j] :
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i]

print(array)