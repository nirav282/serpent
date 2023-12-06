s1 = {'a','b','c','d','g'}
s1.add('e')
print(s1)

s1 = {'a','b','c','d','g'}
s2 = {'f','g','h','i','j'}
s1.update(s2)
print(s1)

s1 = {'a','b','c','d','g'}
s2 = {1,2,3,4,5}
s3 = s1.union(s2)
print(s3)
