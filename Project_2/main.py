# We are going to write a program that generats a random number and asks the user to guess it.
# if the player's guess is higher than the actual number, the program displays "lower number please ", similarly for "higher number please" if he enter small number or two low number.When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.
# Hint : Use the random module

import random
n=random.randint(1,50)
a=-1
guesses=0
while(a!=n):
    guesses+=1
    a=int(input("Guess the number : "))
    if(a>n):
        print("Lower number please ")
    elif(a<n):
        print("Higher number please :")
    else:
        print(f"You guessed the right number : {n}")

print(f' You have guessed the number {n} correctly in {guesses} attempts')