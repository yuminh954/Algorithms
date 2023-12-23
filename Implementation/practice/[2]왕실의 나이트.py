location = list(input())
move = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] 
# ord()를 사용하여 알파벳의 index를 얻는 방법
# alpha : int(ord(location[0])) - int(ord('a')) + 1
x = alpha.index(location[0]) + 1
y = int(location[1])

cnt = 0
for i in range(len(move)) :
    tmp_x = x + move[i][0] # dx
    tmp_y = y + move[i][1] # dy

    if tmp_x < 1 or tmp_y < 1 or tmp_x > 8 or tmp_y > 8 :
        continue
    cnt += 1

print(cnt)