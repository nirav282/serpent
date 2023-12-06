#Python program to find common elements in three lists using sets
l1 = [1,2,3,4,5]
l2 = [4,5,6,7,8]
l3 = [7,8,9,10]
sets1 = set(l1)
sets2 = set(l2)
sets3 = set(l3)
sets4 = sets1&sets2
sets5 = sets2&sets3
sets6 = sets3&sets1
sets7 = sets1&sets2&sets3
print(list(sets4))
print(list(sets5))
print(list(sets6))
print(list(sets7))

