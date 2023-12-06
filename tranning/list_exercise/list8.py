#Python | Cloning or Copying a list


l1 = [1,2,3,4,5]
l2 = l1 
print(l1)
print(l2)

l1 = [5,6,7,8,9]
l2 = l1.copy()
print(l1)
print(l2)

import copy
l1 = [4,5,6]
l2 = copy.copy(l1)
print(l1)
print(l2)