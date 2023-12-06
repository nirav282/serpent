#Python | Check if two lists have at-least one element common
s1 = [1,2,3,4,5]
s2 = [4,5,6,7,8]
sets1 = set(s1)
sets2 = set(s2)
sets3 = sets1&sets2
print(list(sets3))

list1 = [1,2,3,4,5,6]
list2 = [6,7,8,9,10]
found_common = False
for element in list1:
    if element in list2:
        found_common = True
        break
if found_common:
    print("The lists have at least one common element.")
else:
    print("The lists do not have any common elements.")
