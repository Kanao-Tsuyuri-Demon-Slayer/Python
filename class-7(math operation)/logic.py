# Examples of the AND operator
x = True
y = False

result1 = x and y  # Result is False
result2 = x and x  # Result is True
result3 = y and y  # Result is False


# Examples of the OR operator
a = True
b = False

result4 = a or b    # Result is True
result5 = a or a    # Result is True
result6 = b or b    # Result is False


# Examples of the NOT operator
p = True
q = False

result7 = not p  # Result is False
result8 = not q  # Result is True


# Example of using logical operators in an if statement
age = 25
has_license = True

if (age >= 18 and has_license):
    print("You can drive.")
else:
    print("You cannot drive.")
