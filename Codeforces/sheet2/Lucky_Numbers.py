# Lucky Numbers

a,b=map(int,input().split())
lucky_found=False

for i in range(a ,b+1):
    s=str(i)
    is_lucky =True

    for ch in s:
        if ch !='4' and ch !='7':
            is_lucky =False
            break

    if is_lucky:
        print(i,end=" ")
        lucky_found=True

if not lucky_found :
    print(-1)



  