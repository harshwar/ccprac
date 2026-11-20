import numpy as np

print("----------------------------")
n = int(input("Enter number of elements : "))

print("Enter the inputs")
inputs = [] 
for i in range(0, n):
    ele = float(input())
    inputs.append(ele) 
print("Inputs:", inputs)

print("Enter the weights")
weights = []  
for i in range(0, n):
    ele = float(input())
    weights.append(ele)
print("Weights:", weights)

print("The net input can be calculated as yin = x1w1 + x2w2 + x3w3")
yin = []
for i in range(0, n):
    yin.append(inputs[i] * weights[i])

x = round(sum(yin), 3)
print("Net Input (yin):", x)

y1 = 1 / (1 + np.exp(-x))
y2 = (1 - np.exp(-x)) / (1 + np.exp(-x))

print("Output using binary sigmoidal function: ", y1)
print("Output using bipolar sigmoidal function:", y2)
print("----------------------------------")
