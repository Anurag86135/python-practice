#Way too Long Words

num=int(input())

for i in range(num):
    n=input()

    if len(n)<=10:
      print(n)
    else:
       print(n[0]+str(len(n)-2)+n[-1])
