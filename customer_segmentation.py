print("Script started successfully")

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Step 1 – Load the dataset
# -----------------------------
data = pd.read_csv('onlineRetail.csv', encoding='ISO-8859-1')
print("Dataset preview:")
print(data.head())

# -----------------------------
# Step 2 – Clean data and compute RFM
# -----------------------------
# Drop rows where CustomerID is missing
data = data.dropna(subset=['CustomerID'])

# Convert InvoiceDate to datetime format
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

# Create TotalPrice column
data['TotalPrice'] = data['Quantity'] * data['UnitPrice']

# Set reference date for Recency calculation
reference_date = data['InvoiceDate'].max() + pd.Timedelta(days=1)

# Aggregate RFM values
rfm = data.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (reference_date - x.max()).days,
    'InvoiceNo': 'nunique',
    'TotalPrice': 'sum'
})

# Rename columns
rfm.rename(columns={
    'InvoiceDate': 'Recency',
    'InvoiceNo': 'Frequency',
    'TotalPrice': 'Monetary'
}, inplace=True)

print("\nRFM table preview:")
print(rfm.head())

# -----------------------------
# Step 3 – Normalize the data
# -----------------------------
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm)

# -----------------------------
# Step 4 – Elbow Method to find optimal clusters
# -----------------------------
wcss = []
for k in range(1, 10):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(rfm_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 10), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# -----------------------------
# Step 5 – Apply K-Means clustering
# -----------------------------
# Choose the number of clusters based on the elbow plot (e.g. 3)
k = 3
kmeans = KMeans(n_clusters=k, random_state=42)
rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

print("\nRFM with cluster labels:")
print(rfm.head())

# -----------------------------
# Step 6 – Visualize clusters
# -----------------------------
sns.pairplot(rfm, hue='Cluster', diag_kind='kde')
plt.show()
# -----------------------------
# Step 7 – Save clustered data
# -----------------------------
rfm.to_csv('customer_segments.csv')
print("Clustered data saved to 'customer_segments.csv'")