#Python Set difference to find lost element from a duplicated array
a1 = [1, 2, 3, 4, 5]
b1 = [2,3,4,5]
c1 = list(set(a1)-set(b1))
print(c1)

a1 = [1, 2, 3, 4, 5,6]
b1 = [2,3,4,5]
c1 = set(a1).difference(set(b1))
print(list(c1))

a1 = [1, 2, 3, 4, 5]
b1 = [2,3,4,5]
s1 = set(a1)
s2 = set(b1)
s1.difference_update(s2)
print(list(s1))


a1 = [1, 2, 3, 4, 5]
b1 = [2,3,4,5]
s1 = set(a1)
s2 = set(b1)                
s3 = s1 ^ s2                # symmetric_difference_update , symmetric_difference
print(list(s3))

