#Python | Find missing and additional values in two lists
#l1 = [1,2,3,4]
#l2 = [3,4,5,6]
#s1 = set(l1)
#s2 = set(l2)
#s3 = s1.difference(s2)
#print(s3)               
#
#l1 = [1,2,3,4]
#l2 = [3,4,5,6]
#s1 = set(l1)
#s2 = set(l2)
#s3 = s2.difference(s1)
#print(s3)   

l1 = [1,2,3,4]
l2 = [3,4,5,6]
miss_l2 =list(set(l1)-set(l2))   #missing 
addi_l2 =list(set(l2)-set(l1)) # common 
print(miss_l2)
print(addi_l2)
