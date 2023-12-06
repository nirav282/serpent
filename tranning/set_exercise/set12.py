#Python | Check if a given string is binary string or not

binary = {'0','1'}
s1 = input("enter the string:")
u_s = set(s1)

if u_s.issubset(binary):
    print("binary")
else:
    print("not binary")
