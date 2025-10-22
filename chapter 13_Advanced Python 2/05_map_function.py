# Map Example
from functools import reduce


l=[2,3,4,5,6]
square =lambda x:x*x

sqList=map(square,l)# map function
newList=list(sqList)
print(newList)

# sqList =lambda(map(square,l)) we also could do this

# for i in newList:
#     print(i)

# Filter Example
def even(n):
    if(n%2 ==0):
        return True
    return False
onlyEven=filter(even,newList)
print(list(onlyEven))


# Reduce Function

def sum (a,b):
    return a+b
mul=lambda x,y:x*y


print(reduce(sum,l))
print(reduce(mul,l))