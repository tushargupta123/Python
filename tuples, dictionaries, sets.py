# a = (2,3)
# # tuples are immutable while lists are mutable , i.e, we cannot change the entry in tuple but we have create a new tuple itself 
# # all the functions will work same as of list

# #concatenation
# b = 4,5,6       # this is also a tuple
# c = a+b
# print(c)        # (2, 3, 4, 5, 6)

# # tuple of tuples
# d = (a,b)
# print(d)        # ((2, 3), (4, 5, 6))

# e = a*4
# print(e)        # (2, 3, 2, 3, 2, 3, 2, 3)

# print(max(a))   # 3

# # list to tuple
# li = [1,2,3]
# tuple(li)


# variable length input and output
# def sum(a,b,*more):
#     ans = a + b
#     for i in more:
#         ans += i
#     return ans

# a = sum(2,4,5,6,7)
# print(a)

# def out(a,b):
#     return a + b, a - b, a*b

# a = out(1,2)
# print(a)            # it returns a tuple
# a,b,c = out(2,3)
# print(a,b,c)        # we can store values in different variables


# DICTIONARY

# a = {"the":1, "a":4, 100:"abc", 2.4:2}
# # these are mutuable
# a["the"] = 3
# print(a)

# a = dict([("the",5), ("a",23), (100,34)])
# print(a)

# d = dict.fromkeys(["abc",23,3.4],10)      # it will give all keys the same value
# print(d)

a = {1:2, 3:4, "list":[1,23], "dict": {1: 1, 2:4} , 1:25}
# print(a[1])    # 25 bcs dictionary is muttable hence when we make 1:25 as new key value pair it was actually not new pair but it has chnaged the reference of 1.
# print(a.get('list'))     # anther way
# print(a.get('list',0))         # (key, value) if value of that key is not present in dict then it will just show default value given but that does not mean that it was added in dict
# print(a.keys())                 # all keys only
# print(a.values())                 # all values only
# print(a.items())                 # all pairs

# for i in a:
#     print(i ,a[i])              # looping on pairs
# for i in a.values():
#     print(i)                   # looping on values only

# print(1 in a)           # TRUE , it will check only for keys
# print(25 in a)          # here 25 is a value and not key so FALSE

# # add

# a['tuple'] = (1,2,3)   

# # update

# a[1] = 10
# b = {3:5, "the":"tuhsar"}
# a.update(b)         # if any key is repeated then the value will be updated else new pair will be added
# print(a)

# #delete

# a.pop('tuple')
# del a[3]
# print(a)

# a.clear()       # this will clear dict but dict will still be there
# del a            # it will remove whole dict


# PRINT ALL WORDS WITH FREQUENCY K
# s = "this word has many many word"
# k = 2
# def freq(s,k):
#     words = s.split()
#     d = {}
#     for w in words:
#         d[w] = d.get(w,0) + 1
#     for w in d:
#         if d[w] == k:
#             print(w)

# freq(s,k)
    


# SETS

# a = {"apple","abc",23,2.3}      # set is itself a mutable but it can store only immutable items like int,str,float,complex,tuples
# # we cant access these elements simply
# # set doesnot stores duplicate entries , if there are any duplicate entry it will not print it also

# for i in a:
#     print(i)            # order may not be the same

# a.add('temp')   #add
# b = {'abc', 12}
# a.update(b)         # it will add item which was not already present
# a.remove('temp')
# a.discard(13)       # the only difference bw dicard and remove is that if that item is not in set then discard() will not throw any error , while remove will throw an error
# print(a)            # order may not be same

# functions

# a = {1,2,3,4}
# b = {3,4,5,6}
# print(a.intersection(b))  
# print(a.union(b))
# print(a.symmetric_difference(b))
# print(a.difference(b))
# a.intersection_update(b)                  # sets 'a' to intersection set of 'a' and 'b'
# a.symmetric_difference_update(b)
# a.difference_update(b)
# print(a)

# c = {3,4}
# d = {7,8,9}
# print(c.issubset(a))
# print(a.issuperset(c))
# print(a.isdisjoint(d))



# SUM OF UNIQUE NUMBERS
def sum_unique(li):
    s = set()           # to initialize set we can't use s = {} so we have to use s = set()
    for i in li:
        s.add(i)
    sum = 0
    for j in s:
        sum += j
    print(sum)

sum_unique([1,2,3,4,1,2,7])