#Python | Intersection of two lists

l1 = [1,2,3,4,5]
l2 = [4,5,6,7,8]
l3 = set(l1).intersection(set(l2))
print(l3)


l1 = [1,2,3,4,5]
l2 = [4,5,6,7,8]
s1 = set(l1)
s2 = set(l2)
s1.intersection_update(s2)
print(s1)
