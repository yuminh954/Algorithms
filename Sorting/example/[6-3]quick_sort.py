# 1. pivot(기준) 데이터 설정
# 2. pivot 왼쪽에서 pivot 보다 큰 데이터 찾기
# 3. pivot 오른쪽에서 pivot 보다 작은 데이터 찾기
# 4. 2,3번 데이터 swap
# 5. 진행하다가 각 방향의 index가 엇갈렸다면
# 6. 오른쪽 작은 데이터와 pivot을 swap (이를 기준으로 pivot 기준 작은 값, 큰 값으로 분할 됨)
# 7. 분할된 data들 끼리 반복하여 quick sort 
# 8. input array의 원소가 1개이면 종료
# ! python 에서는 pivot과 swap할 필요 없이 list 내 for loop를 활용하여 간단하게 분할 가능

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array) :
    if len(array) <= 1 :
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))