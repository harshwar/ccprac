# Practical 8A: Neural Network with Binary and Bipolar Activation Function
# Sample test inputs:
# Case 1: x = 0.9, w = 0.3, b = 0.32
# Case 2: x = -0.1, w = 0.3, b = -0.2

x = float(input("Input x (e.g. 0.9 or -0.1): "))
w = float(input("Weight w (e.g. 0.3): "))
b = float(input("Bias b (e.g. 0.32 or -0.2): "))

# Calculate Net Input
yin = b + (x * w)

# Binary Activation Function
if yin >= 0:
    y1 = 1
else:
    y1 = 0

# Bipolar Activation Function
if yin >= 0:
    y2 = 1
else:
    y2 = -1

# Display Results
print("Input x =", x)
print("Weight w =", w)
print("Bias b =", b)
print("Net Input yin =", yin)
print("Binary Activation Output y1 =", y1)
print("Bipolar Activation Output y2 =", y2)
