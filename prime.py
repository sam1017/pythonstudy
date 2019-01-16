import time
from math import sqrt
def is_prime(n):
    if n <= 1:
            return False
    for i in range(2,int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
m = 2
n = 100000
prime_list = []
start = time.clock()
for i in range(m, n):
    if(is_prime(i)):
        prime_list.append(i)
t = time.clock() - start
#print(prime_list)
print("find prime range( " + str(m) + ","+ str(n) + ") using time ..")
print(t)