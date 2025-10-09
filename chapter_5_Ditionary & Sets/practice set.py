# #write a program to create a dictionary of  Hindi words with values as thieir english
# # translation.provid user with an option to look up!
# words={
#     "arbitaty":"random",
#     "inquisitive":"curious",
#     "anxious":"worried",
#     "releavant":"related"

# }
# word=input("Enter the word that you want to seach and see its meaning in hindi")
# if word in words:
    
#         print("the meaning of the word :",words[word])
# else:
#     #  print(words.get(word,"The word is not present in the dictionary"))
#         print("nahi kahi or ya Google se puch le 🙏")



# 2).write a program to input eight numbers from the user and display all the unique numbers(Once).
s=set()
# num=input("Emter the number :")
# s.addint((num))
# num=input("Emter the number :")
# s.addint((num))
# num=input("Emter the number :")
# s.addint((num))
# num=input("Emter the number :")
# s.addint((num))
# num=input("Emter the number :")2

# s.addint((num))
# num=input("Emter the number :")
# s.addint((num))
# num=input("Emter the number :")
# s.addint((num))
# num=input("Emter the number :")
# s.addint((num))
# print (s)

# with the hepl of loop
for i in range(8):
    num=input(f"Enter the number{i+1} :")
    s.add(int(num))
# print("the number in uique way is given below {}: ".format(s))
print(s)