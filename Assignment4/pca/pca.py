import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import TSNE
import umap.umap_ as umap
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('pca_data_online_1.txt', sep=' ', header=None)


print("Checking for missing values...")
missing_values = data.isnull().sum().sum()
print(missing_values)


sample_features = data.columns[:10] 
data[sample_features].hist(bins=20, figsize=(15, 10))
plt.tight_layout()
plt.savefig('feature_distributions.png')
plt.close()


corr_matrix = data[sample_features].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Heatmap of Sample Features')
plt.savefig('correlation_heatmap.png')
plt.close()

# we are going to standardize the data
print("\nStandardizing the data...")
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Here we are going to compute the covariance matrix
print("Computing the covariance matrix...")
cov_matrix = np.cov(data_scaled, rowvar=False)

# here we are going to compute the eigenvalues and eigenvectors
print("Computing eigenvalues and eigenvectors...")
eigen_values, eigen_vectors = np.linalg.eigh(cov_matrix)

# Sorting the eigenvalues and corresponding eigenvectors
sorted_index = np.argsort(eigen_values)[::-1]
sorted_eigenvalues = eigen_values[sorted_index]
sorted_eigenvectors = eigen_vectors[:, sorted_index]


print("Projecting the data onto the first two principal components...")
data_pca = np.dot(data_scaled, sorted_eigenvectors[:, :2])


plt.figure(figsize=(8, 6))
plt.scatter(data_pca[:, 0], data_pca[:, 1], s=50, alpha=0.7)
plt.title('PCA Projection onto First Two Principal Components')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.savefig('pca_2d_scatter.png')
plt.close()

print("Creating t-SNE plot...")
tsne = TSNE(n_components=2, random_state=42)
data_tsne = tsne.fit_transform(data_scaled)
plt.figure(figsize=(8, 6))
plt.scatter(data_tsne[:, 0], data_tsne[:, 1], s=50, alpha=0.7)
plt.title('t-SNE Plot')
plt.xlabel('t-SNE Component 1')
plt.ylabel('t-SNE Component 2')
plt.savefig('tsne_plot.png')
plt.close()

print("Creating UMAP plot...")
reducer = umap.UMAP(n_components=2, random_state=42)
data_umap = reducer.fit_transform(data_scaled)
plt.figure(figsize=(8, 6))
plt.scatter(data_umap[:, 0], data_umap[:, 1], s=50, alpha=0.7)
plt.title('UMAP Plot')
plt.xlabel('UMAP Component 1')
plt.ylabel('UMAP Component 2')
plt.savefig('umap_plot.png')
plt.close()
