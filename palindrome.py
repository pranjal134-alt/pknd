list1=[1,2,34]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("palindrome")
else:
    print("non palindrome4" ) 
def is_palindrome(s):
    s=s.replace(" ", "").lower()
    return s == s[::-1]
print(is_palindrome("anA"))
import csv

with open("csk.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
f=open('tv.csv','r') 
data=f.read()
print(data)       
