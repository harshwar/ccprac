# Practical 11: Hebb Rule with Bipolar Inputs and Targets - ANDNOT Function
# Truth table for Bipolar ANDNOT:
# Inputs X1: [1, 1, -1, -1]
# Inputs X2: [1, -1, 1, -1]
# Target Y:  [-1, 1, -1, -1]

x1 = []
x2 = []
y = [-1, 1, -1, -1]

print("Enter 4 Bipolar X1 values (standard: 1, 1, -1, -1):")
for i in range(0, 4):
    e1 = float(input(f"X1[{i+1}]: "))
    x1.append(e1)
print("Bipolar X1 Inputs Are:", x1)

print("Enter 4 Bipolar X2 values (standard: 1, -1, 1, -1):")
for i in range(0, 4):
    e2 = float(input(f"X2[{i+1}]: "))
    x2.append(e2)
print("Bipolar X2 Inputs Are:", x2)

print("Target y ANDNOT =", y)

w1 = 0
w2 = 0
b = 0

for i in range(0, 4):
    w1 = w1 + x1[i] * y[i]
    w2 = w2 + x2[i] * y[i]
    b = b + y[i]

print("Final weights and bias:")
print("w1 =", w1)
print("w2 =", w2)
print("b =", b)
