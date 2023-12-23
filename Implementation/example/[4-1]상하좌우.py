num = int(input())
directions = input().split()

x = 1
y = 1
move_types = ["L", "R", "U", "D"]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(len(directions)) :
    for j in range(len(move_types)) :
        if directions[i] == move_types[j] :
            x_tmp = x + dx[j]
            y_tmp = y + dy[j]
            break

    if x_tmp < 1 or y_tmp < 1 or x_tmp > num or y_tmp > num:
        continue
    x = x_tmp
    y = y_tmp

print(x, y)