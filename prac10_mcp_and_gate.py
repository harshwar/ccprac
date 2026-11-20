
print("--------------------------------------")
print("AND Gate using McCulloch-Pitts Neuron")
print("--------------------------------------")

inputs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

weights = [1, 1]

threshold = 2

for x in inputs:
    weighted_sum = (x[0] * weights[0]) + (x[1] * weights[1])
    if weighted_sum >= threshold:
        output = 1
    else:
        output = 0
    print("Input:", x, " Weighted Sum:", weighted_sum, " Output:", output)

print("--------------------------------------")
