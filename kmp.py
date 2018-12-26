def get_next(find_string):
    next = []
    next.append(-1)
    for index in range(1,len(find_string)):
        t = next[index-1]
        #print("index = " + str(index) + " begin t = " + str(t))
        while t >= 0 and find_string[t + 1] != find_string[index]:
            t = next[t]

        #print("index = " + str(index) + " middle t = " + str(t))
        if find_string[t + 1] == find_string[index]:
            next.append(t + 1)
        else:
            next.append(-1)
        #print("index = " + str(index) + " append : " + str(next[-1]))

    return next


test_string = "0000000000000000000000000000000000000001"
find_string = "00000001"

next = get_next(find_string)

#print(find_string)
#print(str(next))
i = 0
j = 0
while (i < (len(test_string))) and j < len(find_string):
    print("beging i = " + str(i) + " j = " + str(j))
    if j == -1 or test_string[i] == find_string[j]:
        i = i + 1
        j = j + 1
    else:
        j = next[j]
    print("end i = " + str(i) + " j = " + str(j))

print(test_string)
if j == len(find_string):
    print("find string : " + find_string + " at : " + str(i - j))
else:
    print("not find string : " + find_string)