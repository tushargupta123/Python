# def fact(n):
#     n_fact = 1
#     for i in range(1, n+1):
#         n_fact = n_fact * i
#     return n_fact

# n = int(input())
# r = int(input())
# n_fact = fact(n)
# r_fact = fact(r)
# n_r_fact = fact(n-r)
# ans = n_fact//(r_fact*n_r_fact)
# print(ans)


# a1 = 10 #global variable

# def f1():
#     b1 = 12 #local variable
#     print(b1)
#     print(a1) => f1 can access this variable because it is global

# print(a1)
# f1()
# print(b1) #cant access local variabl outside the function
# print(c1)  #cannot access a variable before it is declared
# c1 = 20


# a4 = 13
# def f4():
#     a4 = 12
#     print(a4)
#     print(id(a4))

# print(a4)   # => 13
# f4()        # => 12
# print(a4)   # => 13
# print(id(a4)) # it will print different address then in function bcs python will take the locally declared variable to be local only for that function and will allocate a different memory


# a4 = 13
# def f4():
#     global a4
#     a4 = 12
#     print(a4)
#     print(id(a4))

# print(a4)   # => 13
# f4()        # => 12
# print(a4)   # => 12
# print(id(a4)) # this time it will print same address bcs we have used the global variable inside function too 


# def f1(a, b, c = 0):
#     return a + b + c

# print(f1(2,4))
# print(f1(4,4,3))

# def f1(a=0,b,c):     #we cannot do this as default variables should always come at end 
#     return a + b + c



# Filter , map , reduce

from functools import reduce

nums = [2,4,5,7,8,9,10,11,12]
evens = list(filter(lambda x: x%2==0, nums))        # filter(function, iterable) => it will find the elements which will fulfill the condition. => it gives an object
doubles = list(map(lambda x: x*2, evens))           # map(function, iterable) => it will pick element from iterables and then apply function on it. => it gives an object
sum = reduce(lambda a,b: a+b,evens)                 # reduce(function, iterable) => it will take all elements from iterable and then apply function as a whole on it. => it gives int as answer
print(evens,doubles,sum)



# Types of arguments in functions

# 1. Multiple arguments
def func1(name,message):
    print('hi',name,message)
func1('ajay','welcome')

# 2. Default argument
def func2(name,message="welcome"):
    print("hi",name,message)
func2('ajay')               # hi ajay welcome
func2('ajay','thank you')   # hi ajay thank you
# default argument should always come at end

# 3. keyword argument
def func3(name,message):
    print("hi",name,message)
func3(name="ajay",message="welcome")
# func3(name="ajay",'welcome')        # ERROR - keyword argument should come at end

# 4. Arbitrary argument
def func4(*names):
    for name in names:
        print(name)
func4("ajay","tushar","dj","akg")


