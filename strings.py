# str = '''it is
# used for
# multi line code'''
# print(str)

# name = "tushar"
# print("hello",name,"is")

# strings are immutable ,i.e, we have to store the whole string and we cannot change only one letter but we can access any letter by str[2]


# concatenation

# a = "red" + "blue"
# print(a)
# a = "red" + 3       # we cannot add string and int
# a = "red" + str(3)
# print(a)

# same things which we have used in list can be used for SLICING STRING


# in and not in
# str = "hello"
# if "he" in str:
#     print("it is in string")
# if "heo" not in str:
#     print("not in string")      # it is true bcs heo is not a substring of str.


# comaprison opeartors
# a = "tushba" >= "tushar"
# print(a)            # true bcs it will compare b with a and b > a hence and when it gets such value then after that it stops comparing after values


# functions on string

# split
# str = "my name is tushar tushar tushar"
# print(str.split(" ",2))       # (from where to split, how many splits)

# # replace
# print(str.replace("tushar","gupta",2))      # (what to replace, with what to replace, how many to replace) , by default how many = all

# # find
# print(str.find("tushar",16,24))             # (what to find, range form where to find) , it prints starting index of that element , by default range is all and it will give index of first found element

# # lower and upper
# print(str.upper())
# print(str.lower())


# replacing characters

# def replace(str, char1, char2):
#     newStr = ""
#     for char in str:
#         if char == char1:
#             newStr += char2
#         else:
#             newStr += char
#     return newStr

# str = "aabaab"
# str = replace(str, "a", "c")
# print(str)


# print number of vowels, consonants , digits , special character

# def find(str):
#     v,c,d,s =  0, 0, 0, 0
#     for char in str:
#         if ((char >='a' and char <="z") or (char >= 'A' and char <= 'Z')):
#             char = char.lower()
#             if (char == "a" or char == "e" or char == "i" or char == "o" or char == "u" ):
#                 v += 1
#             else:
#                 c += 1
#         elif (char>= "0" and char<= "9"):
#             d += 1
#         else:
#             s += 1
#     return v,c,d,s

# str = "a12d@# "
# v,c,d,s = find(str)
# print(v,c,d,s)


# Join function
# a = 'ab'.join('abcd')       # 'a' ab 'b' ab 'c' ab d __
# print(a)            # aabbabcabd

# a = 'ab'.join(['1', "2", "3", "4",])
# print(a)            # 1ab2ab3ab4