import matplotlib.pyplot as plt

x = [1,2,3,4]
# plt.plot(x)
# # plt.show()

y = [1,3,6,9]
# plt.plot(x,y)
# # plt.show()

# plt.plot([1,4,6,8,10],[12,34,44,56,23])
# plt.show()

# if we have only single plot at the end then it will show all the plots on the same graph




# plt.figure(1)
# plt.plot([1,4,6,8,10],[12,34,44,56,23])
# plt.figure(2)
# plt.plot(x,y)
# plt.figure(1)
# plt.plot(x)
# plt.show()

# in this way we can show two plots on one graph and another on another graph 


# different ways of representing the plot

# plt.plot(x,y,c="red",linewidth="5",label="Data1",linestyle="dashed",marker="o",markerfacecolor="grey",markersize="10")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.legend()                # it is the mini box which is used to differentiate bw plots
# plt.title("My data")
# plt.xlim(2,9)
# plt.ylim(2,9)
# plt.show()



# ploting data including for loop

# p = 1000
# r = 0.05
# t = 20
# values = []
# for i in range(t+1):
#     values.append(p)
#     p+=p*r
# plt.plot(values)
# plt.grid(x)
# plt.show()




# different type of plots
# plt.bar(x,y,color="k")          # k is color code for black
# plt.hist(x)
# plt.pie(x)
# plt.scatter(x,y)              # it is like normal dotted graph without joining the dots
# plt.show()







# PANDAS PLOT FUNCTION
import pandas as pd

name = ["tushar","devansh","akg","gaurav"]
heigth = [112,323,292,90]
weight = [23,444,21,22]
df = pd.DataFrame({"Name":name,"Height":heigth,"Weight":weight})
df.plot(kind="bar",x='Name',title="vital statistics",color=['green','red','k','c'],linewidth=2,linestyle="dashdot")
plt.ylabel("weight in kg and heigth in cm")
plt.show()

df = pd.DataFrame({"h":heigth})
df.plot(kind="box",title="Box comparison")
plt.show()