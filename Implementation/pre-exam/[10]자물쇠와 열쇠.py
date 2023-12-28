# https://school.programmers.co.kr/learn/courses/30/lessons/60059
def rotate(key) : # 배열 회전 외워두기
    row_len = len(key)
    col_len = len(key)
    
    res = [[0] * row_len for _ in range(col_len)]
    for row in range(row_len) :
        for col in range(col_len) :
            res[col][row_len -1 -row] = key[row][col] 
            
    return res

def check(new_lock) :
    n = len(new_lock) // 3
    for i in range(n, n*2) :
        for j in range(n, n*2) :
            if new_lock[i][j] != 1 :
                return False
    return True
    
def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    new_lock = [[0] * (n*3) for _ in range(n*3)] # 크기 3배 new_lock 
    
    for i in range(n) : # attach
        for j in range(n) :
            new_lock[n+i][n+j] = lock[i][j]
            
    for rotation in range(4) :
        key = rotate(key)
        for x in range(n*2) : # new_lock. (n*2)
            for y in range(n*2):
                for i in range(m): # key
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock) == True:
                    return True
                else :
                    for i in range(m): # detach
                        for j in range(m):
                            new_lock[x+i][y+j] -= key[i][j]
    return False