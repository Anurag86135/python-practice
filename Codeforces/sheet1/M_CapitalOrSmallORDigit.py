# Capital or small or Digit

x=input()

ascii=ord(x)

if x.isdigit():
    print("IS DIGIT")
elif 65<=ascii<=90:
    print("ALPHA")
    print("IS CAPITAL")
elif 97<= ascii<=122:
    print("ALPHA")
    print("IS SMALL")
    

