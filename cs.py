import csv 
cleaned_rows=[]
with open ("data.csv","r") as f:
  reader = csv.DictReader(f)
  for row in reader:
      cleaned_rows.append(row)
print(cleaned_rows)
import pandas as pd
df=pd.DataFrame({"age" : [23,78,65,78,43],
                "marks" : [56,78,89,44,78]})
print(df)
a=df[df["age"]>50]
print(a)
print(df.iloc[0:2]["age"])
c=df.groupby("age").mean()
print(c)
d=df.sort_values("age",ascending=False)
print(d)