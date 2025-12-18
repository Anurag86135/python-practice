# check Power of Two

def PowerTwo(n):
    
   if n>0 and(n&(n-1)) ==0:
       return True 
   else:
       return False
    
n=int(input())
result=PowerTwo(n)
if result is True:
    print("YES")
else:
    print("NO")