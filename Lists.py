# li = [1,2.4,"john"]
# # major difference bw list and array is that we can store elements of different data type in list and can store elements of only same data type in array.
# # list store the references and not the data actually and it stores them in contionus way
# # list maintains that continuity using resizing , when a new element is stored it will create a new list at different location and then copy the previous references in it. 
# len(li)  # gives length of list

# # slicing of a list
# print(li[1:3])   # index 1 and 2 will be printed not 3 will be printed
# li[1:]           # from 1 to last index present
# li[:]            # print the whole list

# # inserting the elements in list
# li.insert(0, 3)     #(index, element)
# li.append(9)        # element will automatically append at last index
# li.insert(9, "santa")  # here 9th index is not present so "santa" will append automatically at end
# li.extend([2,3,4])     # it will insert all three elements in list as different entity
# print(li)   # [3, 1, 2.4, 'john', 9, 'santa', 2, 3, 4]

# # removing elements from list
# li.remove(3)    # if there are more than one 3 then it will remove 3 which occurs first
# li.pop()        # removes last element
# li.pop(6)       # remove element at 6th index
# print(li)       # [1, 2.4, 'john', 9, 'santa', 2]

# # looping in list
# # => looping by index
# for i in range(len(li)):
#     print(li[i])        # prints the whole list

# for i in range(2,len(li)):
#     print(li[i])        # starts printing from 2nd index

# # => looping without index
# for ele in li:
#     print(ele)          # whole list

# for ele in li[2:]:
#     print(ele)          # starts printing from 2nd index

# for ele in li[2:4]:
#     print(ele)          # from 2nd idex to 3rd index


# # sequence in list
# li[2:5:2]               # [start : stop - 1 : step] same rules as of range


# # line separated input
# n= int(input())
# for i in range(n):
#     li.append(int(input()))
# print(li)


# space separated input
# li2 = [int(x) for x in input().split()]      # by default split will split sentence by space and it will be a  string so we have to convert it into int as well
# for ele in li2:
#     print(ele)


# linear searching
# n = int(input())
# found = False
# for ele in li2:
#     if ele == n:
#         print("Found!")
#         found = True
#         break
# if found is False:
#     print("Not found!")


# Immutable => variables in pyton are immutable bcs whenever we change the data then its reference gets changed not that the data in memory itself got changed.
# x = 4
# print(id(x))
# x = 5
# print(id(x))
# here both are different

# Mutable => list in python are mutable bcs whenever we change any one data in list then its reference remains same 
# li = [1,2,3]
# print(id(li))
# li[1] = 4
# print(id(li))
# here both are same

# its reference get changed only when whole list is created from started
# li = [1,2,3] 
# print(id(li))
# li = [1,3]
# print(id(li))
# here both are different 


# Immutable example
# def increment(a):
#     return a + 1
# a = 2
# increment(a)
# print(a)        # it will print 2 bcs varibale is immutable

# Mutable example
# def change(li):
#     li[0] = li[0] + 2
#     return li
# li = [1,2,3]
# change(li)
# print(li)       # it gets changed bcs elements of list is mutable


# reversing a list

# 1
# def reverse_l(li):
#     length = len(li)
#     for i in range(length//2):
#         li[i],li[length-i-1] = li[length-i-1],li[i]         # swapping in python

# li = [1,2,3,4,5,6]
# reverse_l(li)
# print(li)

# 2
# def reverse_l(li):
#     length = len(li)
#     for i in range(length//2):
#         li[i],li[-i-1] = li[-i-1],li[i]         # using negative indexing

# li = [1,2,3,4,5,6]
# reverse_l(li)
# print(li)

# 3
# li = [1,2,3,4,5,6]
# print(li[::-1])         # using sequence , by default start = -1, end = -6 when step = -1