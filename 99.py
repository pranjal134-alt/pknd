import pandas as pd
import numpy as np
dict1={
    "name":["pranjal","tinu","kanu","vidhan"],
    "marks":[56,55,54,57],
    "city":["kohlapur","virhapur","rampur","kanpur"]
}
df=pd.DataFrame(dict1)
print(df)
t=df.to_csv("friends.csv")
print(t)
s=df.tail(2)
print(s)
# a=df.dropna
# print(a)
# k=df.describe()
# print(k)
l=dict1["marks"][0]
print(l)
harry={
    1:{"name":"virat"},
    2:{"name":"kholi"}
}
harry[1]["name"]=["vr"]
print(harry)
p=df.head(1)
print(p)
print(dict1["marks"])
n=df. to_csv("virat_index_false_csv",index=False)
print(n)
ser=pd.Series(np.random.rand(34))
print(type(ser))
newdf = pd.DataFrame(np.random.rand(334,5),index=np.arange(334))
print(newdf)
newdf[0][0]="PRANJAL"
print(newdf.index)
#k=newdf.to_numpy()
k=newdf.T
print(k)
# import pandas as pd
# DI={
#     "NAME":["PRANJAL","TINU"],
#     "MARKS":[34,34]
# }
# data=pd.DataFrame(DI,index=[8,9])
# print(data)
I=pd.read_csv("friends.csv")
print(I)
#m=newdf.loc[0,0]=343
newdf.columns= list("ABCDE")
print(newdf)
newdf.loc[0,"B"]=43
print(newdf.head(3))
newdf.drop("E",axis=1)
print(newdf)
l=newdf.loc[[1,7],["C"]]
print(l)
c=newdf.loc[(newdf["B"]<0.2)]
print(c)
v=newdf.iloc[0,3]
print(v)
#z=newdf.drop(['A','B','C'],axis=1,inplace=True)
Z=newdf.reset_index(drop=True,inplace=True)
print(Z)
print(newdf)
#newdf=newdf["B"].isnull()
newdf.loc[:,['B']]=None
print(newdf)
df.drop_duplicates(subset=["name"])
print(df)
