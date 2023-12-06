#Python set to check if string is pangram
s1 = set('abcdefghijklmnopqrstuvwxyz')
u_i = input("enter the string:").lower()

us = set(u_i)

if us issubset(s1):
    print("pangram")
else:
    print("not pangram")