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