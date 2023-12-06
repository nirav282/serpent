#Python | Difference between two lists
l1 = [10,11,12,13]
l2 = [12,13,14,15]
l3 = list(set(l1)-set(l2))
print(l3)

l1 = [10,11,12,13]
l2 = [12,13,14,15]
l3 = list(set(l2)-set(l1))
print(l3)

l1 = [10,20,30,40]
l2 = [30,33,40,15]
l3 = set(l1).difference(set(l2))
l4 = set(l2).difference(set(l1))
print(list(l3))
print(list(l4))
