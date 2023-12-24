N = list(input())

left_end_idx = len(N) // 2
first_sum = 0
second_sum = 0

for i in range(len(N)) :
    if i < left_end_idx :
        first_sum += int(N[i])
    else :
        second_sum += int(N[i])

if first_sum == second_sum :
    print("LUCKY")
else :
    print("READY")