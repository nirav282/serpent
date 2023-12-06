#print odd numbers in a List
l1 = [12,11,13,56,2,17,88,66,77,76]
l2 = []
for num in l1:
    if num % 2 != 0:
        l2.append(num)
print(l2)