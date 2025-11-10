# first_list=[]
# print(first_list)
# Second_list=[[123,33],[24,"Anurag",False]]#List of lists
# print(Second_list)

Third_list=["Anurag","Ragini","Meena","Ganesh",2,4]#list of Strings and multiple datatype
'''print(len(Third_list))#how len() functio works

Third_list.append('Anshul')#appaend at last in the list
print(Third_list)
print(len(Third_list))
Third_list.insert(1,"Didda")#insert value at 1 index of the list
print(Third_list)

Third_list.remove(4)#first occurnence remove
print(Third_list)'''

# Append and extend
# list=["Lali","Bhai"]
# # Third_list.append(list) #list me list aa jaygi
# Third_list.extend(list)# elements ki tarah na ki list ki tarah
# print(Third_list)

# NOV 6 
#sorted()//copy nabata hai assign karna padega
# sort()//usi list me sort kardega
# list=["banana","apple","mango","kiwi","graphes"]
# num=[22,33,22,44,55,11]
# print(list[0])
# print(num[0])
# print(list[-1])#//end wala print hoga
# print(list[-2])
# print(list)

# for i in list:
#     print(i)

# length=len(list)
# print(length)
    
# list.append("papaya")
# print(list)

# for i in list:
#     print("I like "+ i)

# list.insert(1,"Black berry")
# print(list)

# list.remove("Black berry")
# print(list)

# list.pop()
# print(list)# last value hatt jayga

# del list[-1]
# print(list)

# a=[1,2]
# b=[3,4]
# print(a+b)

# if "apple" in list:
#     print("yes")

# if "apple" not in list: check present or not in the given list
#     print("NO")
# sum=0
# for i in num:
#     sum+=i
# print(sum)

# avg=sum/len(num)
# print(avg)

# max=num[0]
# for i in num:
#     if(i>max):
#         max=i
# print(max)

# min max

# print(max(num))
# print(min(num))
# count=0
# for i in num:
#     if(i ==22):
#         count=count+1

# print(count)
# print(num.count(22))

# character=['x','y','x']
# element='y'
# for i in range(len(character)):
#     if(character[i]==element):
#         print(i)

# num2=[1,1,2,2,3,3,4,4]
# for i in num2:
#     if(i==3):
#         print(num2.index(i))
#         break

# Reverse the list
# list=["banana","apple","mango","kiwi","graphes"]

# list.reverse()
# print(list)
        
# # UpperCase every element of the list
# list2=[]
# for i in list:
#     list2.append( i.upper())


# print(list2)

# alternate way 

# for i in range(len(list)):
#     list[i]= list[i].upper()


# print(list)

# print(num.index(22))



# print(num[0:4])(lst)

# 10 Nov

# list=[2,3,2,4,3,5,5]#
# seen=[]
# out=[]
# for x in list:
#     if x not in seen:
#      seen.append(x)
#      out.append(x)
# print(out) #[2,3,4,5]


# find two numbers whoes sum is that target number we have to find the index of these two numbers
nums = [2, 4, 3, 6, 7]   # Example list
# target = 10
# ans=None
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == target:
#             ans=[i,j]
#             break
#     if ans:break
# print(ans)

# Write a programs in which you need to calculate the sum of every two previous consistent numbers till last print each steps
# sum=0
# for i in nums:
#     sum+=i

#     print(sum)



# Write a program in which we need to take all zero's of the list and put all zero's into last of the list
# list=[0,1,2,0,0,2,4]
# out=[]
# zero=0
# for i in list:
#     if i==0:
#         zero+=1
#     else:
#         out.append(i)

# print(out)

# for i in range(zero):
#     out.append(0)
# print(out)


# write a program in which you will find every term which holds 'a' character inside itself that words and return its count

list=["Ram","Shyam","Anurag","hello"]
count=0
for i in list:
    for char in i:
        if char == 'a':
            print("a is present in", i)
            count+=1
            break

print(count)

        




