default = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
#default = [13,-3, 16,-5, 9]
def sum_value(values):
    sum = 0
    print(values)
    for value in values:
        sum = sum + value
    print(sum)
    return sum

def find_maxmiddlevalue(values, middle):
    find_first = -1
    first_sum = -9999999
    total= 0;
    print("begin find_maxmiddlevalue")
    print(values)
    for i in range(0,middle)[::-1]:
        total = total + values[i]
        if total > first_sum:
            find_first = i
            first_sum = total
    print(str(find_first) + " sum = " + str(first_sum))
    find_second = 0
    second_sum = -99999
    total = 0
    for j in range(middle, len(values)):
        total = total + values[j]
        if total > second_sum:
            find_second = j
            second_sum = total
    print(str(find_second) + "sum = " + str(second_sum))
    print("end find_maxmiddlevalue")
    print(values[find_first:find_second+1])
    return values[find_first:find_second+1]

def find_maxsubarray(values):
    print("find_maxsubarray ")
    print(values)
    if len(values) <= 2:
        return values
    elif len(values) > 2:
        middle = int(len(values)/2)
        print("middle")
        print(middle)
        first = find_maxsubarray(values[0:middle])
        print("first")
        print(first)
        second = find_maxsubarray(values[middle+1:len(values)])
        print("second")
        print(second)
        middle_value = find_maxmiddlevalue(values, middle)
        if sum_value(first) >=  sum_value(second):
            result =  first
        else:
            result =  second

        if sum_value(result) >= sum_value(middle_value):
            return result
        else:
            return middle_value

new_values = find_maxsubarray(default)
print(new_values)

