# t=() #empty tuple

# #tuple having integers
# t=(1,2,3)
# print(t)

# #tuple with mixed datatypes
# t=(1,'raju',34,'abc')
# print(t)
# # # #nested tuple
# # t=(1,(2,3,4),[1,'raju',28,'Anurag'])
# # print(t)


# # t=("Anurag")
# # b=("Anurag",)
# # c="anurag", #bracket here optional

# # print(t)
# # print(type(t))#string
# # print(type(b))#tuple
# # print(type(c))#tuple

# # t=('anurag','murli',"naveen")
# # print(t[2]) indexing

# # nested tuple
# t=('abc',('anurag','purple'))
# print(t[1])
# # print(t[1][1])//purple

# #slicing
# t=(1,2,3,4,5,6)
# print(t[1:4])
# print(t[:-2])#print elements from starting to 2nd last element
# print(t[:])#print element from starting to end

# t[1]=8
# print(t)#TypeError: 'tuple' object does not support item assignmen

# tl=('abc',['anurag','purple'])
# tl[1][1]="Mishra"
# print(tl)#yanha pe ho jayga becos of list

# Concatinating tuples
# t=(1,2,3)+(4,5,6)
# print(t)

# t=(('Anurag',)*5)#repeating
# print(t)

# del t[0]

# print(t)
t=(1,2,3,1,3,3,4,1)
# print(t.count(1))#repeating term

# print(t.index(3))

#exist or not
print(3 in t)

#len
print(len(t))

#sort
new_t=sorted(t)
print(new_t)
print(max(new_t))
print(min(new_t))
print(sum(new_t))
