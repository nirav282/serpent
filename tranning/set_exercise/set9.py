#Python program to count number of vowels using sets in given string
s1 = "prajapatinirav"
vowels = "aeiouAEIOU"

count = 0
for i in s1:
    if i in vowels:
        count +=1
        print(list(i))
print(count)