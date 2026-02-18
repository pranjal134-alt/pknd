import pandas as pd
df=pd.DataFrame({"Name":["A","B","C","D"],"Age":[23,34,45,56],"City":["X","Y","Z","W"]})
print(df)
a=df.to_csv("data.csv")
print(a)
    