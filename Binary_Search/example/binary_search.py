# 시작점, 중간점, 끝점
# 찾고자 하는 데이터와 중간점의 데이터를 반복적으로 비교
# 찾고자 하는 데이터가 중간 데이터보다 작다면, 끝점을 중간점 이전으로,(중간점 포함 이후는 확인할 필요 없음)
#                             크다면, 시작점을 중간점 이후로 설정 (중간점 포함 이전은 확인할 필요 없음)
# 중간 데이터가 찾고자 하는 데이터라면 종료

def binary_search (array, target, start, end) :
    while start <= end :
        mid = (start + end) // 2
        if array[mid] == target :
            return mid
        elif array[mid] < target :
            end = mid - 1
        else :
            start = mid + 1
    return None # start가 end와 같거나 커질 때까지 target을 찾기 못한 경우

n, target = list(map(int, input.split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None :
    print("There is no target value.")
else :
    print(result + 1) 
