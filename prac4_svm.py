# Practical 4: Support Vector Machine (SVM) Classification
# Input dataset: iris.csv (features: sepal & petal dimensions, target: species)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix

# Load the Iris dataset
iris = pd.read_csv("iris.csv")
data = pd.DataFrame(iris)

# Divide dataset into features and target
x = data.drop("species", axis=1)
y = data["species"]

# Split data into training and testing (test_size=0.2, random_state=50)
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=50
)

# Model creation and training
model = SVC(kernel='linear')
model.fit(x_train, y_train)

# Test the model
prediction = model.predict(x_test)
print("Predicted Values:\n", prediction)

# Accuracy of the model
accuracy = accuracy_score(y_test, prediction)
print("Accuracy of the Model:", accuracy)

# Confusion Matrix
cm = confusion_matrix(y_test, prediction)
print("Confusion Matrix:\n", cm)
