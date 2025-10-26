import math

radius= 42
degree=60

#finding the arc length
ArcLength=(degree/360)*2*math.pi*radius

#finding the side of the square
side =ArcLength/4

#finding the Area 
area=side**2

print(f"length of the wire( ArcLength) : {ArcLength}")
print(f"Side of  the square :{ side}")
print(f" Area of the square : {area}")# Area of square