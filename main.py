import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("spotify.csv")

df = df.drop(columns=['Unnamed: 0'])

X = df[['danceability', 'energy', 'loudness', 'tempo', 'valence']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


wcss = []
for i in range(1, 10):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 10), wcss)
plt.title("Elbow Method")
plt.xlabel("Clusters")
plt.ylabel("WCSS")
plt.savefig("elbow.png")
plt.show()

kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

plt.figure(figsize=(8,6))
plt.scatter(df['danceability'], df['energy'], c=df['Cluster'])
plt.xlabel("Danceability")
plt.ylabel("Energy")
plt.title("Spotify Clustering")
plt.colorbar(label="Cluster")
plt.savefig("clustering.png") 
plt.show()

print(df.groupby('Cluster').mean(numeric_only=True))