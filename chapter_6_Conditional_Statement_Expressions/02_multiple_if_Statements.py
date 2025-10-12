# using two or more multiple if independent statement in a program

a=int(input("Enter the age  mere bhai"))

#If statement no:1
if(a%2==0):
    print("a is  even")
#End of  IF statement no:1

if(a>100):
    print("bahoot age hai bhai aapki")

#if statement no:2
if(a>=18):
    print("YOU are above the age of 18 or equal")
elif(a<0):
    print("negative:")
else:
    print("you are below")
    #End of IF statement no:2;

print("End of program")