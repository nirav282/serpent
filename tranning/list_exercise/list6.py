#Different ways to clear a list in Python
l1 = [1,2,3,4,5,5]
l1.clear()
print(l1)


l1 = [1,2,3,4,5,5]
del l1[:]
print(l1)


l1 = [1,2,3]
l1.pop()
l1.pop()
l1.pop()
print(l1)

l1 = [1,2,3]
l1 *= 0
print(l1)

l1 = [1,2,3]
l1.remove(1)
l1.remove(2)
l1.remove(3)
print(l1)