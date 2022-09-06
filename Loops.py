# ****
# ****
# ****
# ****

# n = int(input())
# i = 1
# while i <= n:
#     j = 1
#     while j <= n:
#         print("*",end="")
#         j = j + 1
#     print()
#     i = i + 1

# 4321
# 4321
# 4321
# 4321

# n = int(input())
# i = 1
# while i <= n:
#     j = 1
#     while j <= n:
#         print(n-j+1,end="")
#         j = j + 1
#     print()
#     i = i + 1

# 1
# 23
# 345
# 4567

# n = int(input())
# i = 1
# while i <= n:
#     j = 1
#     p = i
#     while j <= i:
#         print(p,end="")
#         j = j + 1
#         p = p + 1
#     print()
#     i = i + 1 


# 1        
# 2 3      
# 4 5 6    
# 7 8 9 10 

# n = int(input())
# i = 1
# p = 1
# while i <= n:
#     j = 1
#     while j <= i:
#         print(p,end=" ")
#         j = j + 1
#         p = p + 1
#     print()
#     i = i + 1 


# Print the Kth alphabet

# k = int(input())
# x = ord('A')                    #ord gives ascii code for any alphabet
# asciiTarget = x + k - 1         
# targetChar = chr(asciiTarget)   #chr give alphabet related to any ascii value
# print(targetChar)


#    *
#   **
#  ***
# ****

# n = int(input())
# i = 1
# while i<=n:
#     spaces = 1
#     while spaces <= n - i:
#         print(" ",end="")
#         spaces = spaces + 1
#     stars = 1
#     while stars <= i:
#         print("*",end="")
#         stars = stars + 1
#     print()
#     i = i + 1


#    1
#   121
#  12321
# 1234321

# n = int(input())
# i = 1
# while i <= n:
#     spaces = 1
#     while spaces <= n - i:
#         print(" ",end='')
#         spaces = spaces + 1
#     j = 1
#     p = 1
#     while j <= i:
#         print(p, end="")
#         j = j + 1
#         p = p + 1
#     p = i - 1 
#     while p >=1:
#         print(p,end="")
#         p = p - 1
#     print()
#     i = i + 1


# FOR LOOP

# s = "tushar"
# for c in s:
#     print(c)

# n = int(input())
# for i in range(0, n+1 ,1):      #(start , stop-1, step)
#     print(i)

# n = int(input())
# for i in range(n+1):      #(0 , stop-1, 1) if one argument then it will be stop , by default value of start is 0 and step is 1
#     print(i)

# n = int(input())
# for i in range(1,n+1):      #(1 , stop-1, 1) if two argument then first will be start and second will be stop
#     print(i)

# n = int(input())
# for i in range(n, 0 , -1):      # for down counting
#     print(i)


# for printing multiple of 3 within a given range

# a = int(input())
# b = int(input())

# if a % 3 == 0:
#     s = a
# elif a % 3 == 1:
#     s = a + 2
# else:
#     s = a + 1
# for i in range(s , b+1, 3):
#     print(i)


#    1
#   232
#  34543
# 4567654

# n = int(input())
# for i in range(1, n+1, 1):
#     for s in range(n-i):
#         print(" ",end="")
#     for j in range(i , 2*i, 1 ):
#         print(j, end="")
#     for j in range(2*i-2, i-1 , -1):
#         print(j, end="")
#     print()


# Else with loops

# n = int(input())
# for d in range(2 , n , 1):
#     if n%d == 0:
#         break
# else:
#     print("prime number")

    # if loop is ended bcs of break then else will not work otherwise else will work once after loop is finished


# continue => skips a single iteration
# break => breaks the whole loop