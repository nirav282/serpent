marks_input = int(input("enter the marks:"))
result = ""
if marks_input < 30:
   result = "Failed"
elif marks_input > 75:
   result = "Passed with distinction"
else:
   result = "Passed"

print(result)

