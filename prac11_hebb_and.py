x1 = []
x2 = []
y = [1, -1, -1, -1]

print("\nEnter Bipolar X1 Input = ")
for i in range(0, 4):
    e1 = float(input())
    x1.append(e1)
print("Bipolar X1 Inputs Are: ", x1)

print("Enter Bipolar X2 Input = ")
for i in range(0, 4):
    e2 = float(input())
    x2.append(e2)
print("Bipolar X2 Inputs Are: ", x2)

print("Target y AND = ", y)

w1 = 0
w2 = 0
b = 0

for i in range(0, 4):
    w1 = w1 + x1[i] * y[i]
    w2 = w2 + x2[i] * y[i]
    b = b + y[i]

print("w1 = ", w1)
print("w2 = ", w2)
print("b = ", b)
print("\n")