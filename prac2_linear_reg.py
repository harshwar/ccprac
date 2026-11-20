# Practical 2: Linear Regression Example using Scikit-learn
# Input values used for prediction: [[1, 2, 3]]
import random
from sklearn.linear_model import LinearRegression

# Create empty lists for features and target values
feature_set = []
target_set = []

# Number of training samples
number_of_rows = 200
limit = 2000

# Generate random training data
for i in range(number_of_rows):
    x = random.randint(0, limit)
    y = random.randint(0, limit)
    z = random.randint(0, limit)
    # Target value based on a linear equation
    g = 10 * x + 2 * y + 3 * z
    feature_set.append([x, y, z])
    target_set.append(g)

# Create the Linear Regression model
model = LinearRegression()

# Train the model
model.fit(feature_set, target_set)

# Test data (Input values: x=1, y=2, z=3)
test_data = [[1, 2, 3]]

# Predict the output
prediction = model.predict(test_data)

# Display prediction and learned coefficients
print("Prediction for [1, 2, 3]:", prediction)
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
