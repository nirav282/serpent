s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = s1 | s2             #marge  
print(s3)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = s1 & s2        #intersection   (common)
print(s3)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}   #s1-s2 then s2-s1 then (s1-s2)union(s2-s1) 
s3 = s1 ^ s2       #symmetric (not include common)
print(s3)