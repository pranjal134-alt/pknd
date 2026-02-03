# df.describe()
# df.info()
# df.std()
# df.mean()
# df.corr()
# df.count()
# df.max()
# df.min()
# df.median()
import pandas as pd
list=[34,21,56,43]
df=pd.DataFrame(list,range(1,5))
print(df.mean())
'''k=df.to_csv("tv.csv")
print(k)'''
l=pd.read_csv("tv.csv")
print(l)
print(l.shape)
k=l.iloc[2,1]
print(k)
l.loc[0,2]=23
print(l)
df=df[1].isnull()
print(df)
df.columns =("ABCD")
print(df)
