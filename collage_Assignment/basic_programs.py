# factorial

# def fact(n):
#     result=1
#     for i in range(2,n+1):
#         result *=i
#     return result

# print(fact(5))

# # through recursion

# def fact(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n *fact(n-1)
# print(fact(5))

# # 2) febo nachi number or series
# def febo_iterative(n):
#    a,b=0,1

#    for i in range(n):
#        print(a , end=" ")
#        a , b = b , a + b

# febo_iterative(10)

# through Recursion

def febo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return febo(n-1)+ febo(n-2)
    
n=int(input("Enter number nth term :" ))
for i in range(n):
    print(febo(i),end=" ")



        
        