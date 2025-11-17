# Float or int

n=input().strip()
num=float(n)

if num==int(num):
    print("int",int(num))

else:
  int_part=int(num)
  dec_part=num-int_part
  print(f"float {int_part} {dec_part:.3f}")
