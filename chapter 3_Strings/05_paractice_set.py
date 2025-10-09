# 1.)Wrtie a python program to display a user entered name followed by good After noon using input() ffunction
name=input("Enter your name please sir :")
# print("Good AfterNoon",name," sir")
print(f"Good Afternoon {name} Sir ji")

# 2).Write a program to fill in a letter template given below with name and date.
letter='''dear <|Name|>,
You are selected!
<|Date|>'''
print(letter.replace("<|Name|>","Anurag").replace("<|Date|>","20 Dec 2025"))