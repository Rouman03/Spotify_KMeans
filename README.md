# Spotify Songs Clustering using K-Means

## Project Overview

This project applies K-Means clustering to a Spotify songs dataset in order to group songs based on their audio features. The goal is to identify patterns in music and categorize songs into meaningful clusters without using predefined labels.

## Objective

The objective of this project is to analyze song characteristics and group similar songs together using an unsupervised machine learning approach. This helps in understanding how songs differ in terms of energy, mood, and overall style.

## Dataset

The dataset used in this project contains various audio features of Spotify tracks such as danceability, energy, loudness, tempo, and valence. These features are used as input for clustering.

## Features Used

- Danceability
- Energy
- Loudness
- Tempo
- Valence

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib

## Methodology

1. The dataset is loaded using Pandas.
2. Relevant features are selected for clustering.
3. Data is standardized using StandardScaler to ensure all features contribute equally.
4. The Elbow Method is used to determine the optimal number of clusters.
5. K-Means clustering is applied to group the songs.
6. The clusters are visualized using scatter plots.
7. Cluster characteristics are analyzed using mean feature values.

## How to Run

1. Clone the repository
2. Navigate to the project folder
3. Create a virtual environment
4. Install dependencies
5. Run the script

## Output

The project produces:

- Elbow Method graph to determine optimal clusters
- Scatter plot showing clustered songs
- Summary of cluster characteristics

## Algorithm Used

K-Means Clustering is an unsupervised learning algorithm that groups data points into clusters based on similarity. It works by minimizing the distance between points within the same cluster.

## Conclusion

The project successfully groups songs into clusters based on their audio features. These clusters can represent different types of songs such as high-energy tracks, calm songs, or balanced compositions. This approach can be extended to build recommendation systems or analyze user preferences.

## Author

Rouman Syed Nazeer
