# Pascal Triangle

def Pascal(num):
    for i in range(1,num+1):
        val = 1
        for j in range( i):
            print(val, end=' ')
            val=val*(i-j-1)//(j+1)
            
        print()

num=int(input())
Pascal(num)