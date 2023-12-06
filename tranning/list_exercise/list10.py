#Find sum and average of List in Python

l1 = [10,20,30,40]
l2 = sum(l1)
avg = l2 / len(l1)
print(l2)
print(avg)


l1 = [10,20,30,40]
l2 = sum(l1[:])
avg = l2 / len(l1)
print(l2)
print(avg)