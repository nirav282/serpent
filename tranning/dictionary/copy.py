d1 = {'a':10,'b':20,'c':40,'d':50,'e':60}
d2 = d1

print(d1)
print(d2)
d1["b"] = 100
print(d1)
print(d2)#reflect

d1 = {'a':10,'b':20,'c':40,'d':50,'e':60}
d2 = d1.copy()
print(d1)
print(d2)
d1["b"] = 100
print(d1)
print(d2)# not reflect
