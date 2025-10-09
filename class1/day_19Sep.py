# //check pallindrome#
# text = "madam"
# is_pallindrome = True
# for i in range (len(text)//2):
#     if text [i] != text[-(i+1)]:
#         is_pallindrome =False
#         break
# if is_pallindrome:
#     print(f"'{text}' is a pallindrome")
# else:
#     print(f"'{text}' is not a pallindrome")


# 2. //wordCount
# sentence ="I am a good boy"
# count=0
# word =""
# for ch in sentence+" ":
#     if ch !=" ":
#         word+=ch
#     else:
#         if word !=" ":
#             count +=1
#             word ="" 
# print(f" the sentence has {count} words")
        

# //hamstrong 

# num= 153
# power =len(str(num))
# total =0
# for digits in str(num):
#     total+=int(digits)**power
# print(num,"is armstrong ?",total==num)


# 4.// Triangle pattrerns using numbers

# rows = 5
# for i in range (1,rows +1):
#     for j in range (1,i+1):
#         print(j,end =" ")
#     print()
    

# 5.# sum digit until single digit

# 6 // strong number

num=145
total=0
for i in str(num):
    digit =int(i)
    fact =1
    for i in range(1,digit+1):
        fact*=i
    total +=fact
if total ==num:
    print(f"{num} is strong number")
else:
    print(f"{num} is not a strong number")



