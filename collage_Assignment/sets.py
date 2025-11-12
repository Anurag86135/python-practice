# set of integers
# s={1,2,3}
# print(s)

# print type of s
# print(type(s))


# s={1,2,3,3,1,4}
# print(s)#dont allow duplicates items


# we can make set from a list
# s= set([1,2,3,1])
# print(s)#//here set is behaving like an function

# ?set indexing not support

# s={1,2}

# set object doesn't support indexing
# print(s[0])


# s.add(24)
# print(s)

# s.update([5,6,7])#adding multiple items
# print(s)

# add list and set
# s.update([8,9],{10,2,3})
# print(s)

# s.discard(3) #remove like in list remove particular item in a set
# print(s)


# s.pop()#random value will delete
# print(s)

# s.clear()# all element will clear inside the set
# print(s)

# //operations of set
# set={1,2,3,4}
# set2={3,4,4,5}
# print(set|set2)

# print(set.union(set2))


# #intersection
# print(set & set2)
# print(set.intersection(set2))

# # difference
# print(set-set2)#those elements that are in set but not in set 2

# print(set.difference(set2))
# #  semantic difference
# print(set^set2)
# print(set.symmetric_difference(set2))

# subset

# x={"a","b","c","d","e"}
# y={"c","d"}
# print("set 'x' is subset of 'y' ?",x.issubset(y))
# print("set 'y' is subset of 'x' ?",y.issubset(x))

#Frozen Sets
# immutable hota hai

# set1=frozenset([1,2,3,4])
# set2 =frozenset([3,4,5,6])
# #try to add element into set gives an error
# set1.add(5)#)AttributeError: 'frozenset' object has no attribute 'add'

# rest operation will work like normal set istead of add,update and so on

# in a list of strings we find a charcter which will be common in all the strings element?

lst=["Ram","Ghansyam","Aman","Rahul"]



s1 = set(lst[0])
for i in range(1, len(lst)):
    s = set(lst[i])
    s1 = s1 & s
print(s1)


