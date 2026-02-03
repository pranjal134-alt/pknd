import numpy as np
# myarr=np.array([[23,54,4,2],[3,2,5,6]])
# print(myarr)
k=np.ones((1,23))
print(k)
import pandas as pd
list=[2,1,3]
df=pd.DataFrame(list)
print(df)
a=df.to_csv("pranjal.csv_index_false",index=False)
print(a)
import numpy as np
myarr= np.array( [[2,1,3,
                 4,8,2],
                 [4,3,3,
                  3,2,1]
                       ])
                 
b=np.sum(myarr)
a=np.mean(myarr)
print("the sum is ",b,"the avg is ",a)
list=[23,45,82,12] 
print(list.insert(1,3))