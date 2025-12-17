#shiftZeroes

def shift_Zeros(arr,n):
    result= []
    zer_count =0
    #separate non-zero elements and zeros
    for x in arr:
        if x!=0:
            result.append(x)
        else:
            zer_count+=1
    
    #Add zeros at the end

    result.extend([0]*zer_count)

    return result

n=int(input())
arr=list(map(int,input().split()))
#Function call
ans=shift_Zeros(arr,n)

for i in ans:
    print(i,end=" ")

