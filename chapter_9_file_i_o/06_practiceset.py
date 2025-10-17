#1) Write a program to read the text from a given file 'poems.txt and find out whether it contains the word 'twinkle'
# f=open("poem.txt")
# content=f.read()
# if("twinle" in content):
#     print("twinkle is present in the content")
# else:
#     print("not present in this content")
# f.close()

# 2)The game() function in a program lets a user play a game and returns the score as an integer.
# You need to read a file 'hi-score.txt' which is either blank or contains the previous Hi-score.
# You need to write a program to update the h-score whenever the game() function breaks the Hi-score.

import random
def game():
    print("You are playing the game...")
    score=random.randint(1,699)
    #Fetch the hiScore
    with open("hiScore.txt") as f:
        hiScore=f.read()
        if(hiScore!=""):
            hiScore=int(hiScore)
        else:
            hiScore =0
    print(f"Your score : {score}")
    if(score>hiScore):
        #write this hiScore to the file
        with open("hiScore.txt" ,"w") as f:
            f.write(str(score))
    return score

game()
