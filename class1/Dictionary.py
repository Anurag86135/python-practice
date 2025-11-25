# my_dict={}#Empty dictionary

# #dictionary with integer keys
# my_dict={1:'abc',2:'xyz'}
# print(my_dict)

# #dictionar with mixed keys
# my_dict={'name':'satish',1:['abc','xyz']}
# print(my_dict)

# my_dict=dict() #create empty dictionary using dict()
# my_dict=dict([(1,"Anurag"),(2,"Mishra")])#Create a dict with list of tuple
# print(my_dict)

# #Dict Access

my_dict={'name':'satish','age':27,'address':'jabalpur'}
# #get name from key
# print(my_dict['name'])


#if key is not there in dict then error comes =>KeyError
# print(my_dict['degree'])


# #another way of accessing key
# print(my_dict.get('address'))

# #none aayga keyerror nahi ayyaga
# print(my_dict.get('degree'))


#update name
# my_dict['name']="Anurag"
# print(my_dict)

#add new key

# my_dict['degree']='B.tech'
# print(my_dict)

#create a dictionary item
# print(my_dict.pop('age'))
# print(my_dict)


#Remove an arbitary key
# my_dict.popitem()
# print(my_dict)

square={2:3,3:9,4:16,5:25}
#dwlete particular key
# del square[4]

#remove all items
# square.clear()


#delete dictionary itself
# del 

#copy from one to another dictioary
# Dict=square.copy()
# print(Dict)
# print(square)

#fromkeys[seq[,v]] -> Return a new dictioary with keys from seq and value
# subject ={}.fromkeys(['Math','English','Hindi'],0)
# print(subject)

subject={2:2,3:9,4:16,5:25}
# print(subject.items())#return a new view of the dictionary items(key,val)

# # if we want to printonly values or keys then 
# print(subject.keys())
# print(subject.values())


#get list of all available methods and attributes of dictionary
# d={}
# print(dir(d))

#Dictionary comrehenshion
# d={'a':1,'b':2,'c':3}
# for pair in d.items():
#     print(pair)

#Creating a new dictionary with only pairs where the value is larger than 2
# new_dic={k:v for k,v in subject.items() if v>2}
# print(new_dic)


#We can also perform operations on the value pairs
d={'a':1,'b':2,'c':3,'d':4}
d={k+'c':v*2 for k,v in d.items() if v>2}
print(d)