# J.Count Letters

s=input()

for i in 'abcdefghijklmnopqrstuvwxyz':
    count=s.count(i)
    if count>0:
        print(f"{i} : {count}")