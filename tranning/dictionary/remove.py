d2 = {'g':100,'h':1000,'s':100,'k':1000}
del d2['g']
print(d2)

d2 = {'g':100,'h':1000,'s':100,'k':1000}
d3 = d2.pop('h')
print(d3)

d2 = {'g':100,'h':1000,'s':100,'k':1000}
d3 = d2.popitem()
print(d3)

d2 = {'g':100,'h':1000,'s':100,'k':1000}
d2.clear()
print(d2)
