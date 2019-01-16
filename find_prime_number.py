import time
from math import sqrt
prime_number_list = [2]
n = 10000

start = time.clock()
for i in range(3,n):
    is_prime = False
    sqrt_i = int(sqrt(i) + 1)
    for j in prime_number_list:
        if(j <= sqrt_i):
            if i%j == 0:
                is_prime = False
                break
            else:
                is_prime = True
        else:
            break;
    if is_prime == True:
        prime_number_list.append(i)
t = time.clock() - start
#print(prime_number_list)
print("find prime number in range( 2, " + str(n) + ") using time ...")
print(t)
