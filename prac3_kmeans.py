import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

x = [4, 5, 10, 4, 3, 11]
y = [21, 19, 24, 17, 16, 25]
print("x =", x)
print("y =", y)

data = list(zip(x, y))
print("Data Points:", data)

plt.scatter(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

model = KMeans(n_clusters=2, random_state=42)
l
model.fit(data)

print("Cluster Labels:", model.labels_)

print("Cluster Centers:")
print(model.cluster_centers_)

plt.scatter(x, y, c=model.labels_, cmap='viridis')

centers = model.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], marker='X', s=200, color='red', label='Centroids')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
