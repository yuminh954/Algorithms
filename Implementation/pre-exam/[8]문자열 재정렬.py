list = list(input())

alphas = []
nums = []

for i in range(len(list)) :
    if list[i].isalpha() == True :
        alphas.append(list[i])
    else :
        nums.append(int(list[i]))

alphas.sort()

for i in range(len(alphas)) :
    print("{}".format(alphas[i]), end='')
print(sum(nums))