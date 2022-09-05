c1 = 20
c2 = 30
c3 = c2>c1
c4 = c2<c1
print(c3 or c4) #true
print(c3 and c4) #false

n = int(input())
is_even = (n%2 == 0)
if is_even:
    print("number is even")
else:
    print("number is odd")

if n > 10:
    print("number is greater than 10")
elif n>=5:
    print("number is greater than 5 but less than 10")
else:
    print("number is less than 5")


r = int(input())
count = 1
while count <= r:
    print(count)
    count = count + 1 


# sum of even integers

n1 = int(input())
sum = 0
if n1 % 2 == 0:
    while n1 >= 0:
        sum = n1 + sum
        n1 -= 2
    print(sum)


# find weather a number is prime or not

n2 = int(input())
n3 = n2 - 1
flag = False
while n3 >= 2:
    if n2 % n3 == 0:
        flag = True
    n3 = n3 - 1
if flag:
    print("number is not prime")
else:
    print("number is prime")

    