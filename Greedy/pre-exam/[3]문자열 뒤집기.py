string = list(input())
string = [int(_) for _ in string]
pre_num = string[0]
cnt = 0

for i in range(1, len(string)) :
    if string[i] != pre_num :
        cnt += 1
    pre_num = string[i]
if cnt % 2 == 0 :
    result = cnt // 2
else :
    result = cnt // 2 + 1
print(result)