import numpy as np
a=np.array([1,2,6])
print(np.shape(a))
print(a.std())
print(np.unique(a)[0])
d=np.array([1,2,6])
e=d[d>2]
print(e)