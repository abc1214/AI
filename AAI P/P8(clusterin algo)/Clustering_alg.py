import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
import sklearn.metrics as sm
import pandas as pd
import numpy as np
iris = datasets.load_iris()
X = pd.DataFrame(iris.data, columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length',
'Petal_Width'])
y = pd.DataFrame(iris.target, columns=['Targets'])
model = KMeans(n_clusters=3, n_init=10)
model.fit(X)
colormap = np.array(['red', 'lime', 'black'])
plt.subplot(1, 2, 1)
plt.scatter(X.Petal_Length, X.Petal_Width, c=colormap[iris.target], s=40)
plt.title('Red Classification')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.subplot(1, 2, 2)
plt.scatter(X.Petal_Length, X.Petal_Width, c=colormap[model.labels_], s=40)
plt.title('K Means Clustering')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.show()
print('The Accuracy score of K-Means: ',sm.accuracy_score(iris.target, model.labels_))
print('The Confusion matrix of K-Means: ')
print(sm.confusion_matrix(iris.target, model.labels_))