default = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

find_i = 0
find_j = 0
sum = default[0]
for i in range(1,len(default)):
    result = 0
    for j in range(0,i+1)[::-1]:
        result = result + default[j]
        if result > sum:
            find_i = j
            find_j = i
            sum = result

print(default[find_i:find_j+1])
