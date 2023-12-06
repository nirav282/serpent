#Python Program to Accept the Strings Which Contains all Vowels

user = set(str(input("enter the string:")))
vowels = set("AEIOUaeiou") 

if vowels.issubset(user):
    print("The string contains all vowels.")
else:
    print("The string does not contain all vowels.")
    
    
