capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Capital of Gujarat is : ", capitals['Gujarat'])
print ("Capital of Karnataka is : ", capitals['Karnataka'])
#print ("Capital of Karnataka is : ", capitals['hariyana']) #key error

d1 = {'a':1,'b':10}
d2 = {'c':100,'d':1000}
d3 = d1 | d2
print(d3)

d1 = {'a':1,'b':10}
d2 = {'c':100,'d':1000}
d1|= d2
print(d3)

#d1 = {'eaa':1,'faa':10}
#d2 = {'gaa':100,'haa':1000}
#d3=d1.union(d2)
#print(d3)

d1 = {'e':1,'f':10}
d2 = {'g':100,'h':1000}
d1.update(d2)
print(d1)

d1 = {'a':1,'b':10}
d2 = {'g':100,'h':1000}
d3 = {**d1,**d2}
print(d3)

d1 = {'g':100,'h':1000}
d2 = [('j',20),('g',200)]
d1.update(d2)
print(d1)

d1 = {'g':100,'h':1000}
d1.update(nirav=50,neel=10,bhavik=30,krish=80)
print(d1)

marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print (marks)
marks['Laxman'] = 95
print (marks)