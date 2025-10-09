s={1,2,3,4,5}
s2={5,6,7,8}
print(s.union(s2))# it will combine the all element of both the sets
print(s.intersection(s2))# it will print the common elements of both the sets
print(s.issuperset({2,1}))# it will check the given element is present in the set or not and return boolean value
print({7,8}.issubset(s2)) # it will check the given set or element is given on the set 2 or not
print(s.difference(s2))# it will print the elements of set s which are not present in set s2
print(s2.difference(s))# it will print the elements of set s2 which are not present in set s