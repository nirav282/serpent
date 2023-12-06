#print even numbers in a list
l1 = [1,2,3,4,40,33,42,76,66,77,99]
l2 = []
for num in l1:
    if num % 2 == 0:
        l2.append(num)
print(l2)