# import simplemath
# print(simplemath.x)

# simplemath.add(10,20)
# simplemath.product(3,4)

# rename
# import simplemath as m
# m.add(50,80)

# specific function and variable use not all
# from simplemath import add, product

# print(x) it give error bcos we havn't import it
# add(78,12)
# product(5,7)


# member Aliasing:
from simplemath import x as y, add as sum
print(y)
sum(10,20)

