s1 = {'a','b','c','d','g'}
s1.remove('b')
print(s1)

s1 = {'a','b','c','d','g'}
s1.pop()
print(s1)

s1 = {'a','b','c','d','g'}
s1.discard('g')
print(s1)

s1 = {'a','b','c','d','g'}
s1.clear()
print(s1)

s1 = {'a','b','c','d','g'}
s2 = {'i','h','c','d','g'}
s1.difference_update(s2)       #s1 - s2
print(s1)

s1 = {'a','b','c','d','g'}
s2 = {'i','h','c','d','g'}
s3 = s1.difference(s2)       # new set (s1 - s2)
print(s3)

s1 = {'a','b','c','d','g'}
s2 = {'i','h','c','d','g'}
s1.intersection_update(s2)   #common
print(s1)

s1 = {'a','b','c','d','g'}
s2 = {'i','h','c','d','g'}
s3 = s1.intersection(s2)   #common
print(s3)

s1 = {'a','b','c','d','g'}
s2 = {'i','h','c','d','g'}
s1.symmetric_difference_update(s2)    #not include common
print(s1)

s1 = {'a','b','c','d','g'}
s2 = {'i','h','c','d','g'}
s3 = s1.symmetric_difference(s2)   #not include common
print(s3)