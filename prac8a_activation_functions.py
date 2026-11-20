print("------------------------------------")
print("Input x = ")
x = float(input())
print("Weight w = ")
w = float(input())
print("Bias b = ")
b = float(input())

yin = b + (x * w)

if yin >= 0:
    y1 = 1
else:
    y1 = 0

if yin >= 0:
    y2 = 1
else:
    y2 = -1

print("Input x =", x)
print("Weight w =", w)
print("Bias b =", b)
print("Net Input yin =", yin)
print("Binary Activation Output y1 =", y1)
print("Bipolar Activation Output y2 =", y2)
print("------------------------------------")
