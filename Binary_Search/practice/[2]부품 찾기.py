N = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

M = int(input())
m_list = list(map(int, input().split()))

def binary_search(array, target, start, end) :
    while start <= end : 
        mid = (start + end) // 2
        if array[mid] == target :
            return True
        elif array[mid] < target :
            start = mid + 1
        else :
            end = mid - 1
    return False
    
for i in range(M) :
    is_exist = binary_search(n_list, m_list[i], 0, N - 1)
    if is_exist == True :
        print("yes", end = " ")
    else :
        print("no", end = " ")