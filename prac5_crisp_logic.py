# Practical 5: Crisp Logic Membership Operators (in, not in)
# Input values used: a = 10, b = 10, test a = 2 with list [1, 2, 3, 4, 5]
a = 10
b = 10
list_val = [1, 2, 3, 4, 5]

if a in list_val:
    print("Line 1 - a is available in the given list")
else:
    print("Line 1 - a is not available in the given list")

if b not in list_val:
    print("Line 2 - b is not available in the given list")
else:
    print("Line 2 - b is available in the given list")

a = 2
if a in list_val:
    print("Line 3 - a is available in the given list")
else:
    print("Line 3 - a is not available in the given list")
