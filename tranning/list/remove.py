l1 = [1,2,3,4,5,6,7]
l1.remove(2)            #obj base   remove
print(l1)

l1.pop()                 
print(l1)

l1 = [1,2,3,4,5,6,7]
l1.pop(2)              #indexing base
print(l1)

l1 = [1,2,3,4,5,6,7]    #remove 4
del l1[3]              #indexing base
print(l1)

l1 = [1,2,3,4,5,6,7]    #remove 4
del l1[1:4]              #indexing base
print(l1)