import numpy as np
import matplotlib.pyplot as plt
# a=np.array(list(map(int,input("enter the number").split())))
# b=np.array(list(map(int,input("enter the number").split())))
# plt.plot(a,b,linestyle="-",linewidth=3,marker="*")
# plt.grid(color="black")
# plt.show()
# a=np.array(list(map(int,input("enter the number").split())))
# print(np.insert(a,2,34))
r=np.array(list(map(int,input("enter the number").split())))
print(np.delete(r,1))
c=np.array(list(map(int,input("enter the number").split())))
print(r * c)
x=[23,45,35]
plt.hist(x)
plt.grid()
plt.tight_layout()
plt.savefig("india.png")