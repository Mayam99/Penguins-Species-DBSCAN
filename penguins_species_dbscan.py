# -*- coding: utf-8 -*-
"""Penguins Species-DBSCAN.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mKQ-8W1n6srNDw5SroU5i7zc57-3fWVE

#Introduction
###In this notebook, we will explore the application of the DBSCAN (Density-Based Spatial Clustering of Applications with Noise) algorithm to the  Penguins Species dataset. This dataset contains observations of penguin species, and our goal is to uncover natural groupings within the data without prior knowledge of the species labels.

##Why DBSCAN?

###DBSCAN is a powerful clustering algorithm known for its ability to:

* Identify clusters of varying shapes and sizes.
* Handle noise and outliers effectively.
* Operate without needing to specify the number of clusters in advance.

###These characteristics make DBSCAN a suitable choice for our penguin species dataset, where we aim to detect natural clusters and potentially noisy data points.

###About this file

* The dataset consists of 5 columns:

* culmen_length_mm: culmen length (mm)

* culmen_depth_mm: culmen depth (mm)

* flipper_length_mm: flipper length (mm)

* body_mass_g: body mass (g)

* sex: penguin sex

###Source:
https://www.kaggle.com/datasets/youssefaboelwafa/clustering-penguins-species

##Importing Necessary Libraries
"""

import numpy as np #NumPy is a powerful tool for numerical computations in Python.
import pandas as pd  #Pandas is a powerful library for data manipulation and analysis.
import seaborn as sns #Seaborn is a statistical data visualization library based on Matplotlib.
import matplotlib.pyplot as plt #Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.

"""##Reading the Dataset in a pandas dataframe."""

df = pd.read_csv('penguins.csv')

df.head() #Displays the first 5 rows of the dataset.

df.columns #Displays columns names of the dataset.

df.shape #Displays the total count of the Rows and Columns respectively.

df.sample(10) #Displays random samples.

df.info() # Displays the total count of values present in the particular column along with the null count and data type.

df.isnull().sum() # Displays the total count of the null values in the particular columns.

"""Here we can check that, there are some missing values in the dataset."""

df = df.dropna()#Dropping the missing values using the dropna function.

df.isnull().sum()

"""Now as we have alredy dropped the missing values, now there is no missing value."""

df.describe()

"""The df.describe() function in pandas provides a statistical summary of the numerical columns in a DataFrame df. Here’s what it typically includes:

count: The number of non-null observations.

mean: The average of the values.

std: The standard deviation of the values.

min: The minimum value.

25%: The 25th percentile (first quartile).

50%: The 50th percentile (median).

75%: The 75th percentile (third quartile).

max: The maximum value.
"""

df = df.drop(columns=['sex']) #For simplicity, we'll drop the 'sex' column

df.head()

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

# Standardize the data
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df) #Features are standardized to have zero mean and unit variance using StandardScaler.

# Apply DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=2)
clusters = dbscan.fit_predict(df_scaled)

clusters

df['cluster'] = clusters

# Visualize the clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='culmen_length_mm', y='culmen_depth_mm', hue='cluster', palette='viridis', s=100)
plt.title('DBSCAN Clustering of Penguin Data')
plt.xlabel('Culmen Length (mm)')
plt.ylabel('Culmen Depth (mm)')
plt.show()

df['cluster'] = clusters

# Visualize the clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='body_mass_g', y='culmen_length_mm', hue='cluster', palette='viridis', s=100)
plt.title('DBSCAN Clustering of Penguin Data')
plt.xlabel('Body Mass (g)')
plt.ylabel('Culmen Lenght (mm)')
plt.show()