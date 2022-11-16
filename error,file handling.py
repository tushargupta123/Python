# # error handling consists of run time error only 

# a = 5
# b = 2
# try: 
#     print("file opened")
#     print(a/b)
#     k = int(input("enter a number"))
#     print(k)
# except ZeroDivisionError:       # for only any particular type of error
#     print("zero division error")
# except Exception as e:          # for all errors
#     print(e)
# else:
#     print("no error")
# finally:
#     print("file closed")

# # finally will run everytime either try runs or except runs
# # only one out of all except will run
# # else will run only if there is no error and if there is any error then else will not run but finally will run at any cost


# # User defined exception
# class BalanceException(Exception):
#     pass
# def checkBalance():
#     money = 100
#     withdraw = 80
#     balance = money - withdraw
#     if (balance < 30):
#         raise BalanceException("insufficient balance")
#     print(balance)
# try:
#     checkBalance()
# except BalanceException as b:
#     print(b)




# File handling

f = open("myData.txt","r")
# print(f.read())         # reads whole document
# print(f.readline())     # prints first line and after that when used again then prints next line
# print(f.readlines())    # gives list of file in which each line is treated as different element of that list
print(f.read(1))          # gives no. of characters mentioned

f1 = open("abc.txt","w")
# f1.write("something")       # it will simply write on that file
# f1 = open("abc.txt","a")    # this will append the text and will not delete previously written text as "w" will do so
# f1.write("new")

for data in f:
    f1.write(data)