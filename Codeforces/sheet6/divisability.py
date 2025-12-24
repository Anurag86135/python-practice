# Divisability

# def Divisiblility(num):
#     a=num[0]
#     b=num[1]
#     c=num[2]
#     total=0

#     for i in range(a,b+1):
#         if i%c==0:
#             total+=i

#     print(total)

# num=list(map(int,input().split()))
# Divisiblility(num)


def divisiblity():
    a,b,x=map(int,input().split())
    if a>b:
        a,b=b,a

    start =((a+x-1)//x)*x
    end=(b//x)*x
    if start>end: 
        print(0)
    else:
        count =((end-start)//x)+1
        print(count*(start+end)//2)
    
divisiblity()