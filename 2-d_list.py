# li = [[2,3,4],[4,5,6],[6,7]]
# this type of 2d list is called JAGGED LIST bcs column size of every row is not same

# List Comprehension
# [(output) (for loops) (conditions)]

# li = [1,2,3,4,5,6]
# li_new = [ele**2 for ele in li]
# li_new = [ele**2 for ele in li if ele%2 == 0]
# li_new = [ele**2 for ele in li if ele%2 == 0 if ele%3 == 0]    # if element is divisible by 2,3 both , multiple if conditions
# print(li_new)

# li_1 = [1,2,3,4,5]
# li_2 = [1,2,3]
# li_inter = [ele for ele in li_1 for ele2 in li_2 if ele==ele2]     # multiple for loops
# print(li_inter)

# li_new = [ele**2 if ele%2 == 0 else ele for ele in li]          # if else
# print(li_new)

# li = ['tushar','devansh','abhishek']
# li_2d = [[s for s in ele] for ele in li]        # for making 2d list
# print(li_2d)


# taking input in 2d list

# => taking different rows in different line
# str = input().split()
# n,m = int(str[0]),int(str[1])
# li = [[int(j) for j in input().split()] for i in range(n)]
# print(li)

# => taking all the rows in same line
# str = input().split()
# n,m = int(str[0]),int(str[1])
# b = input().split()
# li = [[int(b[m*i+j]) for j in range(m)] for i in range(n)]
# print(li)

# => taking all things in same line
# str = input().split()
# n,m = int(str[0]),int(str[1])
# b = str[2:]
# li = [[int(b[m*i+j]) for j in range(m)] for i in range(n)]
# print(li)


# printing 2d list

# => 1
# li = [[1,2,3,4], [5,6], [7,8,9]]
# for row in li:
#     for ele in row:
#         print(ele, end=" ")
#     print()

# => 2
# li = [[1,2,3,4], [5,6], [7,8,9]]
# for row in li:
#     output = ' '.join([str(ele) for ele in row])
#     print(output)

# Largets Column Sum
# def largest_col_sum(li):
#     n = len(li)
#     m = len(li[0])
#     max_sum = -1
#     highest_index = -1
#     for j in range(m):
#         sum = 0
#         for i in range(n):
#             sum += li[i][j]
#         if sum > max_sum:
#             max_sum = sum
#             highest_index = j
#     return highest_index, max_sum

# li = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
# largest_col_index, largest_col_sum = largest_col_sum(li)
# print(largest_col_sum,largest_col_index)
