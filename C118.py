# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JUBcOFhq3Ut8bJGJF7B0_4FuL8ISTfPJ
"""

from google.colab import files
uploaded=files.upload()

import pandas as pd
import plotly.express as px

df=pd.read_csv("data36253712535621352765.csv")
print(df.head())
fig=px.scatter(df,x="petal_size",y="sepal_size")
fig.show()

from sklearn.cluster import KMeans

x=df.iloc[:,[0,1]].values
print(x)
wcss=[]
for i in range(1,11):
  kmeans=KMeans(n_clusterr=i,init='k-means++',random_state=42)
  kmeans.fit(x)
  wcss.append(kmeans.inertia_)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,5))
sns.lineplot(range(1,11),wcss,marker='o',color='lime')
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

kmeans=KMeans(n_clusters=3,init='k-means++',random_state=42)
y_kmeans=kmeans.fit_predict(x)

plt.figure(figsize=(15,7))
sns.scatterplot(x[y_kmeans==0,0],x[y_kmeans==0,1],color='yellow',label='cluster 1')
sns.scatterplot(x[y_kmeans==1,0],x[y_kmeans==1,1],color='blue',label='cluster 2')
sns.scatterplot(x[y_kmeans==2,0],x[y_kmeans==2,1],color='green',label='cluster 3')
sns.scatterplot(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],color='red',label='Centroids',s=100,marker=',')
plt.grid(False)
plt.title('Clusters of Flowers')
plt.xlabel('Petal size')
plt.ylabel('Sepal size')
plt.legend()
plt.show()