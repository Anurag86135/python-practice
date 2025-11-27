# E_Hady_Rides_ the_ train


N=int(input())

row=N//4
positive=N%4
if row%2==0:
    column=positive
else:
    column=3-positive

print(row,column)

