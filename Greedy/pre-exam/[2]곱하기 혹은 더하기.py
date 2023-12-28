string = input()
result = 0

for i in range(len(string)) :
    if int(string[i]) != 0 and result != 0 :
        result = result * int(string[i])
    else :
        result = result + int(string[i])
    
print(result)