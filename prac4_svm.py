import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix

print("=====================================================")

iris = pd.read_csv("iris.csv")
data = pd.DataFrame(iris)
print(data)

x = data.drop("species", axis=1)
y = data["species"]

print("Feature Set")
print(x)
print("Target Set")
print(y)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=50
)

print("=====================================================")
print("X Train")
print(x_train)
print("=====================================================")
print("X Test")
print(x_test)
print("=====================================================")
print("Y Train")
print(y_train)
print("=====================================================")
print("Y Test")
print(y_test)

model = SVC(kernel='linear')
model.fit(x_train, y_train)

prediction = model.predict(x_test)
print("=====================================================")
print("Predicted Values")
print(prediction)

print("=====================================================")
print("Accuracy of the Model")
accuracy = accuracy_score(y_test, prediction)
print(accuracy)

print("=====================================================")
print("Confusion Matrix")
cm = confusion_matrix(y_test, prediction)
print(cm)
