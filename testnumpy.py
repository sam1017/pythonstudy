import numpy as np

#x = np.array([3,1,2])
#print(np.argsort(x))
#print(np.tile(x,(3,2)))

#x = np.array([[1,3],[2,2]])
#print(np.argsort(x,axis=0))
#print(np.argsort(x,axis=1))

x = np.array([3,1,2])
print(x[np.argsort(x)])
print(x[np.argsort(-x)])
a = x[np.argsort(x)]
print(a[::-1])