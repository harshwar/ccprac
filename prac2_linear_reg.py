import random
from sklearn.linear_model import LinearRegression


feature_set = []
target_set = []

number_of_rows = 200
limit = 2000

for i in range(number_of_rows):
    x = random.randint(0, limit)
    y = random.randint(0, limit)
    z = random.randint(0, limit)
    g = 10 * x + 2 * y + 3 * z
    print(i, "x =", x, "y =", y, "z =", z, "g =", g)
    feature_set.append([x, y, z])
    target_set.append(g)
l
model = LinearRegression()

model.fit(feature_set, target_set)

test_data = [[1, 2, 3]]

prediction = model.predict(test_data)

print("\nPrediction:", prediction)
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

