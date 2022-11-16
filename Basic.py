# python is a interpreter language as its code gets executed line by line and compiler based languages gets compiled at once and then they are executed.


print("hello")
a = 10
b = 20
print(a+b)
# variable name can start form any thing except from digit ex - s12 is fine but 12s is not fine
a = 'abc'
print(a)
# here a does not store the variable itself but it stores the address of variable hence when we change the value of 'a' the value 10 is remained at one address but now the 'a' stores the address of "abc"
print(type(a))
a = 4 + 5j    #Complex numbers
print(a)
print(type(a))
a = 20
b = 20
print(id(a))
print(id(b)) 
# they would have same address for values from -5 to 256 bcs they are more commonly used and if we try to modify both and set them same again then there address would not be same
a = a+1
print(id(a))
# a simple modification will change the address 
c = 25 / 6
print(c) # 4.177 => floating point division
c = 25 // 6
print(c) # 4 => integer point division
d = input() # it will take string
print(type(d))
d = int(input()) # we have to type cast for taking any other type of data
print(type(d))
