#Python program to convert Set into Tuple and Tuple into Set

s1 = {1,2,3,'a','b'}
t1 = tuple(s1)
print(t1)
s1 = set(t1)
print(s1)