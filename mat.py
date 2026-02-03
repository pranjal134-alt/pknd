import matplotlib.pyplot as plt
'''x=[2,3,4,6]
y=[32,34,16,56]
plt.plot_date(x,y)
plt.show()
x=["mon","tue","wed","thu"]
y=[23,21,32,13]
plt.barh(x,y,color="green")
plt.title("bakery sales every day")
plt.xlabel("days")
plt.ylabel("sles per day")
plt.show()
months=[1,2,3,4]
sales=[1000,1700,1500,1300]
plt.plot(months,sales,color="black",linestyle="--",linewidth=2,marker="*",label="2025 sales data")
plt.xlabel("months")
plt.ylabel("sales")
plt.xlim(1,4)
plt.ylim(1000,1800)
plt.xticks([1,2,3,4],["m1","m2","m3","m4"])
plt.legend(loc="upper left",fontsize=10)
plt.grid(color="red")
plt.show()
revenue=[1000,2000,3000,1200]
regions=["north","south","east","west"]
plt.pie(revenue,labels=regions,autopct="%1.1f%%",colors=["red","purple","yellow","green"])
plt.show()
score=[23,12,45,32,12,46,76,32,14,56,32,11,17]
plt.hist(score,bins=5,color="purple",edgecolor="green")
plt.grid(color="black")
plt.show()
hour_std=[1,2,3,4]
stu_marks=[56,67,78,89]
plt.scatter(hour_std,stu_marks,marker="o")
plt.show()'''
x=[1,2,3,4]
y=[23,12,1,4]
plt.scatter(x,y)
plt.grid(color="black")
plt.subplot(1,1,1)
plt.show()
fig ,ax= plt.subplots(1,2, figsize= (10,5))
x=[1,2,3,4]
y=[23,12,1,4]
ax[0].plot(x,y)
ax[0].set_title('line port')
ax[1].bar(x,y,color=["blue","yellow","green","red"])
ax[1].set_title('bar chart')
plt.show()
a=[1,2,3,4]
b=[10,15,20,21]
plt.xlabel("days")
plt.ylabel("sales")
plt.plot(a,b)
plt.savefig("line_plot.png",dpi=300)