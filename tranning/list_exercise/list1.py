#Python program to interchange first and last elements in a list
l1 = [5,2,3,4,1]
l1.pop(0)
l1.insert(0,1)
l1.pop(-1)
l1.append(5)
print(l1)