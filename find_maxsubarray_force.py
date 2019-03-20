default = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

find_i = 0
find_j = 0
max_sum= -999999
for i in range(0,len(default)):
    total = 0
    for j in range(i, len(default)):
        total = total + default[j]
        if total > max_sum:
            find_i = i
            find_j = j
            max_sum = total

print(default[find_i:find_j+1])