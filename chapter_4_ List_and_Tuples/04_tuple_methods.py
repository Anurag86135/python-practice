a=(1,45,342,3424,False,45,"Rohan","shivam",1,1)
print(a)
no=a.count(1)#it will count the value that how many  times it is available in the tuple
print(no)

i=a.index(45)#index dega konse index me ye element hai
print(i)

print(1 in a)# you can check if an elemeent or item exists in atuple 'in' keyword.

repeated =a*3
print(repeated) # tuple can be repeated using '*'operator

print(len(a))#give length of the tuple

sliced=a[1:4]
print(sliced)

my_tuple=(1,2,3)# unpacking:tuple can be unpacked into individual variable
b,c,d=my_tuple
print(b,c,d)