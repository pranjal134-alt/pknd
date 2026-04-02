import pandas as pd
a=pd.read_csv("data.csv")
print(a)
a["City_Name"]=a["City_Name"].str.strip().str.title()
#print(a)
'''a=a[a["City_Name"]=="Venice"]'''
a=a[a["ID"]>15]
e=a.drop_duplicates().sum()
print(e)
a=lambda x,y:x**y
print(a(8,3)).