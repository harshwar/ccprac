# Practical 9: Neural Network with Binary and Bipolar Sigmoidal Activation Function
# Sample test inputs:
# Number of elements: 3
# Inputs: 0.2, 0.4, 0.6
# Weights: 0.1, 0.3, 0.5
import numpy as np

n = int(input("Enter number of elements (e.g. 3): "))

print(f"Enter {n} inputs one by one (e.g. 0.2, 0.4, 0.6):")
inputs = []
for i in range(0, n):
    ele = float(input(f"Input[{i+1}]: "))
    inputs.append(ele)
print("Inputs:", inputs)

print(f"Enter {n} weights one by one (e.g. 0.1, 0.3, 0.5):")
weights = []
for i in range(0, n):
    ele = float(input(f"Weight[{i+1}]: "))
    weights.append(ele)
print("Weights:", weights)

yin = []
for i in range(0, n):
    yin.append(inputs[i] * weights[i])

x = round(sum(yin), 3)
print("Net Input (yin):", x)

y1 = 1 / (1 + np.exp(-x))
y2 = (1 - np.exp(-x)) / (1 + np.exp(-x))

print("Output using binary sigmoidal function:", y1)
print("Output using bipolar sigmoidal function:", y2)
