# O_Calulator
exp=input()

if '+' in exp:
    a,b=map(int,exp.split('+'))
    print(a+b)

elif '-' in exp:
    a,b=map(int,exp.split('-'))
    print(a-b)
elif '*' in exp:
    a,b=map(int,exp.split('*'))
    print(a*b)
elif '/' in exp:
    a,b=map(int,exp.split('/'))
    print(a//b)



