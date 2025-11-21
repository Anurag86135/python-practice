#Converting to decimal

Num=int(input())

for i in range(Num):
    n=int(input())

    ones=bin(n).count("1")#convert n into binary and counts the ones
    binary_String="1"*ones#Make a binary number of only ones
    result=int(binary_String, 2)# convert that binary srting into decimal

    print(result)