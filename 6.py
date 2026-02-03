import numpy as np
k=np.full((2,3),8)
print(k)
l=np.arange(1,3,2)
print(l)
t=np.eye(3)#identity matrixin which diagonal is one other is zero
print(t)
p=np.array([[4,6,8,
            7,8,9],
           [5,6,9,
            7,7,8]
]    )
#k=p.shape
#k=p.size
k=p.ndim
print(p+2)
print(np. std)
p=np.array([[4,6,8,
            7,8,9],
           [5,6,9,
            7,7,8]
]    )
c=np.std(p)
print(c)
t=np.array([4,6,8,7,8,9]  )
print(t[1:3])
print(t[::-1])
print(t[[2,4]])
n=np.eye(3)
print(n)
print(t[t>6])
monti=np.array([[1,6],[2,4]])
z=np.ravel(monti)
print(z)
j=np.insert(monti,1,[3,8])
print(j)
c=np.array([2,3,4])
d=np.array([7,6,5])
b=np.concatenate((c,d))
print(b)
k=np.delete(d,1)
print(k)
l=np.delete(p,0,axis=0)
print(l)
print(p.shape)
print(np.vstack((c,d)))
print(np.split(d,3))
prices=[23,21]
discount=10
final_prices=[]
for price in prices:
    price = price -(price * discount/100)
    final_prices.append(price)
    print(final_prices)
prices=np.array([100,200,300])
dis=19
final_prices=prices-(prices*dis/100)
print(final_prices)  
print(prices.sum()) 
matrix=np.array([[23,32,21],[12,34,12]])
vector=np.array([2,4,5])
result=matrix * vector
print(result) 
j=np.array([6,np.nan])
print(np.isnan(j))
def cal_avg(a,b):
    avg=(a+b)/2
    print(avg)
    return avg
a=int(input("enter the  number"))
b=int(input("enter the number"))
cal_avg(a,b)
list1=[1,2,34]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("palindrome")
else:
    print("non palindrome4" ) 
k=list(map(int,input("enter the number").split()))
print(k)       
import numpy as np
g=np.array([2,3,4,5,6,7])
print(np.insert(g,2,3))
print(np.delete(g,3))
print(np.ndim(g))
print(g.max(),g.min())