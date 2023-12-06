#Concatenated string with uncommon characters in Python

s1 = "asdf"
s2 = "dfgh"
s3 = set(s1) ^ set(s2)               #symmentric_difference_update  #symmentric_difference
print(s3)
print("string:", ''.join(s3))

