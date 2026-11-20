# Practical 3: K-Means Clustering
# Input dataset coordinates: x = [4, 5, 10, 4, 3, 11], y = [21, 19, 24, 17, 16, 25]
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Dataset
x = [4, 5, 10, 4, 3, 11]
y = [21, 19, 24, 17, 16, 25]
print("x =", x)
print("y =", y)

# Merge x and y into coordinate pairs
data = list(zip(x, y))
print("Data Points:", data)

# Plot the original dataset
plt.scatter(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Create the K-Means model with 2 clusters
model = KMeans(n_clusters=2, random_state=42)

# Train the model
model.fit(data)

# Print cluster labels
print("Cluster Labels:", model.labels_)

# Print cluster centers
print("Cluster Centers:\n", model.cluster_centers_)

# Plot the clustered dataset
plt.scatter(x, y, c=model.labels_, cmap='viridis')

# Plot cluster centroids
centers = model.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], marker='X', s=200, color='red', label='Centroids')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
