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

# If you open a file in mode x, the file is created and opened for writing – but only if it doesn’t already exist. Otherwise you get a FileExistsError.
# f2 = open("newText.txt","x")
# f2.write("hey guys")

# f3 = open("abc.txt","x")        # ERROR



# tell()
# File handle is like a cursor, which defines from where the data has to be read or written in the file. Sometimes it becomes important for us to know the position of the File Handle. tell() method can be used to get the position of File Handle. tell() method returns current position of file object. This method takes no parameters and returns an integer value. Initially file pointer points to the beginning of the file(if not opened in append mode). So, the initial value of tell() is zero.

# seek() method
# In Python, seek() function is used to change the position of the File Handle to a given specific position. File handle is like a cursor, which defines from where the data has to be read or written in the file. 
 

# Syntax: f.seek(offset, from_what), where f is file pointer
# Parameters: 
# Offset: Number of positions to move forward 
# from_what: It defines point of reference.
# Returns: Return the new absolute position.

# The reference point is selected by the from_what argument. It accepts three values: 
# 0: sets the reference point at the beginning of the file 
# 1: sets the reference point at the current file position 
# 2: sets the reference point at the end of the file 
 
# By default from_what argument is set to 0.





# Directories
import os

print(os.getcwd())      # retruns current directory
# os.chdir("C://")        # change the working directory
print(os.listdir())     # gives a list of all the sub directories present in that directory
# os.mkdir("/name.txt")
# os.makedirs("/new/file")    # to make directory inside a directory
# os.rename("bholla.txt","bhollu.txt")
# os.remove("bhollu.txt")         # removes file
# os.rmdir("/new/file")                    # it can remove a diretory only if it is empty 