# [note] 내가 쓰는 좌표계 방향, 문제에서 준 좌표계 방향 통일해두고 시작할 것!

N, M = map(int, input().split())
y, x, dir = map(int, input().split())
locations = []
for i in range(N) :
    row = input().split()
    locations.append(row)

dir_list = [0, 1, 2, 3] 
dx_list = [0, 1, 0, -1]
dy_list = [-1, 0 , 1, 0]

locations[x][y] = '2'
cnt = 1
done = False

def turn_left(x, y, dir_idx) :
    for i in range(1, 5) :
        left_dir = dir_list[dir_idx - i]
        dx = dx_list[left_dir]
        dy = dy_list[left_dir]
        tmp_x = x + dx
        tmp_y = y + dy
        if locations[tmp_y][tmp_x] == '0' :
            ret = left_dir
            break
        if i == 4 :
            ret = -1
    return ret

while done == False :
    ret_dir = turn_left(x, y, dir)

    if ret_dir == -1 :
        while True :
            rev_dir = (dir + 2) % 4
            dx = dx_list[rev_dir]
            dy = dy_list[rev_dir]
            tmp_x = x + dx
            tmp_y = y + dy
            if locations[tmp_y][tmp_x] == '1' :
                done = True
                break
            else : 
                x = tmp_x
                y = tmp_y

    else :
        dx = dx_list[ret_dir]
        dy = dy_list[ret_dir]
        x = x + dx
        y = y + dy
        dir = ret_dir
        locations[y][x] = '2'
        cnt += 1
    
print(cnt)