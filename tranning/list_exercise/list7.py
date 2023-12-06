#Reversing a List in Python
l1 = [1,2,3,4]
l1.reverse()
print(l1)

l1 = [1,2,3,4]
print(l1[::-1])

l1 = [1,2,3,4]
l =[]
for i in l1:              
    l.insert(0,i)
print(l)
    

