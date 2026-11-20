# Practical 8B: Neural Network Net Input with Bias
# Sample test inputs: x1 = 0.2, x2 = 0.4, w1 = 0.1, w2 = 0.5, b = 0.3

x1 = float(input("Input x1 (e.g. 0.2): "))
x2 = float(input("Input x2 (e.g. 0.4): "))
w1 = float(input("Weight w1 (e.g. 0.1): "))
w2 = float(input("Weight w2 (e.g. 0.5): "))
b = float(input("Bias b (e.g. 0.3): "))

yin = b + (x1 * w1 + x2 * w2)

print("Input nodes x1 and x2 =", x1, x2)
print("Weight w1 and w2 =", w1, w2)
print("Bias b =", b)
print("Net Input (yin) =", yin)
