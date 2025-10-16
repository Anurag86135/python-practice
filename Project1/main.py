# project 1: we all have played snake water gun game in our childhood . If you have'nt, google the rules of this game and write a python 
# program capable of playing this game with the user.


import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1,0,1])
youstr=input("Enter your choice :")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"snake",-1:"water",0:"Gun"}

you =youDict[youstr]
# by now we have 2 numbers (variables), you and computer

print(f"You choose { reverseDict[you]}\ncomputer choose {reverseDict[computer]}")

if(computer ==you):
    print("its draw😁")
else:
    if(computer ==-1 and you ==1):
        print("You win😎")
    elif(computer ==-1 and you ==0):
        print("You lose😒")
    elif(computer==1 and you==-1):
        print("you lose😒")
    elif(computer==1 and you==0):
        print("you Win😎")
    elif(computer==0 and you==-1):
        print("you Win😎")
    elif(computer==0 and you==1):
        print("You loose😒")
    else:
        print("Something went Wrong😒")



        #  or we can also did this by this method->

        # if(computer-you==2 or computer-you==-1):
        #     print("You lose")
        # else:
        #     print("You win")