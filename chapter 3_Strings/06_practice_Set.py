# 3).Write a program to detect double space in a string.
name="Anurag is a  good  boy"
print(name.find("  "))# it will return the index of the first occurence of the double space and also check that double space is preent or not in that given sentence
# if t is not present then it will return -1.

# 4).Replace the double space from 3 with single spaces
print(name.replace("  "," "))# it will replace the double space with single space
#  print(name) strings are immutable which means that you cannot change them by runing function on them.


#5).write a program to formate the following letters using escape sequence characters.
letter="Dear Anurag, this python course is nice . thanks for giving me this!"
# print(letter)
letter2="Dear Anurag, \n\tThis python course is nice.\nThanks for giving me!"
print(letter2)