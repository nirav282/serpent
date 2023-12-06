l1 = [10,20,10,50,40,10]
l2 = l1.count(10)
print(l2)

l1 = [10,20,10,50,40,10]
counter = 0
x = int(input("enter the num:"))
for i in l1:
    if x == i:
        counter += 1
print(counter)