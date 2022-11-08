# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python (learn-env)
#     language: python
#     name: learn-env
# ---

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# <div style="color:white;
#            display:fill;
#            border-radius:5px;
#            background-color:#5642C5;
#            font-size:200%;
#            font-family:Arial;letter-spacing:0.5px">
#
# <p width = 20%, style="padding: 10px;
#               color:white;">
# K Nearest Neighbors and the Curse of Dimensionality
#               
# </p>
# </div>
#
# Data Science Cohort Live NYC Nov 2022
# <p>Phase 3: Topic 27</p>
# <br>
# <br>
#
# <div align = "right">
# <img src="Images/flatiron-school-logo.png" align = "right" width="200"/>
# </div>
#     
#     

# %% slideshow={"slide_type": "slide"}
import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

# %% [markdown] slideshow={"slide_type": "slide"}
# <center><img src = "Images/neighbor_tyranny.jpg" width = 450/></center>

# %% [markdown] slideshow={"slide_type": "fragment"}
# <center>There's truth here. But we can also rely on this tyranny to help us build classifiers.</center>

# %% [markdown] slideshow={"slide_type": "subslide"}
# <center> Let's do it. </center>

# %% [markdown] slideshow={"slide_type": "slide"}
# #### K-nearest neighbors

# %% [markdown] slideshow={"slide_type": "slide"}
# **Process of predicting in k-nearest algorithm**

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# Take a **test** data point, look at it's $k$ nearest neighbors in **training** set:
#
# - Look at what class neighbors in training set all are.
# - Count class tallies all up.
# - Assign datapoint to winning majority class.

# %% [markdown] cell_style="center" slideshow={"slide_type": "fragment"}
# <center><img src = "Images/knn_3.webp" width = 800/></center>
# <center> k = 3 neighbors </center>

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# - Concept is easy. 
# - Doing this efficiently: exercise in algorithms and data structures.
#
#
# More details:
#
# https://towardsdatascience.com/tree-algorithms-explained-ball-tree-algorithm-vs-kd-tree-vs-brute-force-9746debcd940
#

# %% [markdown] slideshow={"slide_type": "slide"}
# **Process of training k-nearest algorithm**

# %% [markdown] slideshow={"slide_type": "fragment"}
# - Store the training data points.
# - Yeah thats it.

# %% [markdown] slideshow={"slide_type": "slide"}
# #### The role of $k$: number of neighbors

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
#
# <img src = "Images/KNN_nearestnn.png" width = 400 />

# %% [markdown] cell_style="split" slideshow={"slide_type": "fragment"}
# Changing neighbors:
# - Clearly affects which KNN predicts for test point.

# %% [markdown] cell_style="split" slideshow={"slide_type": "fragment"}
# - Lower $k$ implies higher sensitivity to fluctuations (higher variance)
#

# %% [markdown] slideshow={"slide_type": "-"}
# **Low $k$ = higher variance**

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](./images/knn-process.png)

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# If $k$ increases too much:
# - Always predicts majority class in training set.
# - Model too "rigid"
# - Not sensitive enough to relationship between target and features

# %% [markdown] cell_style="split" slideshow={"slide_type": "fragment"}
# <img src = "Images/knn_neighbor_increase.jpeg" width = 600 />

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# Too high $k$ means high bias.

# %% [markdown] cell_style="split" slideshow={"slide_type": "fragment"}
# In summary:
# <center><img src = "Images/bias_variance.png" /></center>

# %% [markdown] slideshow={"slide_type": "slide"}
# #### Before we even think about running this or any distance-based model

# %% [markdown] cell_style="split" slideshow={"slide_type": "fragment"}
# <center>SCALE THE FEATURES!!!</center>

# %% [markdown] cell_style="split" slideshow={"slide_type": "fragment"}
# Otherwise: 
# - Weights distances in different feature dimensions differently

# %% [markdown] cell_style="split" slideshow={"slide_type": "fragment"}
# <center><img src = "Images/nonnormal.png" /></center>
# <center>Unscaled</center>

# %% [markdown] cell_style="split" slideshow={"slide_type": "fragment"}
# <center><img src = "Images/normalized.png" /></center>
# <center>Scaled</center>

# %% [markdown] slideshow={"slide_type": "slide"}
# Run KNN classifier on a dataset and tune hyperparameters:
# - Load that iris dataset.

# %% cell_style="center" slideshow={"slide_type": "fragment"}
iris_df = pd.read_csv('Data/Iris.csv').drop(columns = ['Id'])
iris_df.head()

# %% cell_style="center" slideshow={"slide_type": "slide"}
from sklearn.preprocessing import LabelEncoder
target_transform = LabelEncoder()
iris_df['Species'] = target_transform.fit_transform(iris_df['Species'])

# %% cell_style="center" slideshow={"slide_type": "fragment"}
iris_df['Species']


# %% [markdown] slideshow={"slide_type": "slide"}
# - What next steps should we take?

# %% [markdown] slideshow={"slide_type": "fragment"}
# Visualize the data.

# %% cell_style="split" slideshow={"slide_type": "slide"}
sns.pairplot(hue = 'Species', data = iris_df, height = 1.75)
plt.show()

# %% [markdown] cell_style="split" slideshow={"slide_type": "fragment"}
# For instruction sake let's do classification with following two features:
# - sepal width
# - petal width

# %% cell_style="split" slideshow={"slide_type": "fragment"}
sns.scatterplot(y = 'SepalWidthCm', x = 'PetalWidthCm', hue = 'Species', data = iris_df)
plt.show()

# %% [markdown] slideshow={"slide_type": "slide"}
# Some overlap between class 1 and 2:
# - Virginica
# - Versicolor

# %% [markdown] slideshow={"slide_type": "slide"}
# What next?

# %% [markdown] slideshow={"slide_type": "slide"}
# 1. Separate dataframe into X (features) and y (labels)
# 2. Train/test split

# %% cell_style="center" slideshow={"slide_type": "fragment"}
# so whats next?
X = iris_df[['SepalWidthCm', 'PetalWidthCm']]
y = iris_df['Species']

# %% cell_style="center" slideshow={"slide_type": "fragment"}
# shuffle and split, stratify keeps target distribution same in train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify = y, test_size = 0.15, random_state = 42)

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# Now we standardize features, right?

# %% [markdown] cell_style="split" slideshow={"slide_type": "fragment"}
# Depends!
# - If doing simple train/test split, then yes!
# - If doing cross-validation, then no!

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# Mess around with $k$:
# - Look at performance
# - Hyperparameter tune/cross-validate

# %% [markdown] cell_style="split" slideshow={"slide_type": "fragment"}
# So we won't fit the standardizer on the entire training set.

# %% slideshow={"slide_type": "slide"}
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# %% slideshow={"slide_type": "slide"}
k = KFold(n_splits = 5).split(X_train)


# %% slideshow={"slide_type": "fragment"}
next(k)


# %% cell_style="center" slideshow={"slide_type": "slide"}
def cross_validation(X_train, y_train, k, num_split = 10):
    
    X_train = X_train.values
    y_train = y_train.values
    
    score_train_list = []
    score_val_list = []
    
    for train_index, valid_index in KFold(n_splits = num_split).split(X_train):


        # train and validation splitting 
        X_train_fold, X_val_fold = X_train[train_index], X_train[valid_index]
        y_train_fold, y_val_fold = y_train[train_index], y_train[valid_index]

        #create/fit the Standard scaler on the train fold
        scaler = StandardScaler()
        X_tf_sc = scaler.fit_transform(X_train_fold)
        # transform validation fold
        X_vld_sc = scaler.transform(X_val_fold)

        # create/fit knearest neighbor
        knn = KNeighborsClassifier(n_neighbors = k)
        knn.fit(X_tf_sc, y_train_fold)
        
        # now how did we do?
        accuracy_train = knn.score(X_tf_sc, y_train_fold)
        accuracy_val = knn.score(X_vld_sc, y_val_fold)
        score_val_list.append(accuracy_val)
        score_train_list.append(accuracy_train)
    
    return {'k': k, 'train': np.mean(score_train_list), 'validation': np.mean(score_val_list)}

# %% slideshow={"slide_type": "slide"}
# empty dataframe
crossval_df = pd.DataFrame(columns = ['k', 'train', 'validation'])
# append results for each value of k
for k in np.arange(1,100):
    crossval_df = crossval_df.append(cross_validation(X_train, y_train, k, 5), ignore_index = True)

# %% cell_style="split" slideshow={"slide_type": "slide"}
crossval_df.info()

# %% cell_style="split" slideshow={"slide_type": "fragment"}
fig, ax = plt.subplots()
sns.lineplot(x = 'k', y = 'train', 
             data = crossval_df, 
             ax = ax, label = 'train')
sns.lineplot(x = 'k', y = 'validation', 
             data = crossval_df,
             ax = ax, label = 'validation')
ax.set_ylabel('Accuracy')
ax.set_title('5-fold CV tuning KNN')
plt.show()

# %% [markdown] slideshow={"slide_type": "fragment"}
# Some bias-variance tradeoff in action as a function of $k$.

# %% cell_style="center" slideshow={"slide_type": "slide"}
# let's find our best performing k-value
crossval_df.iloc[crossval_df['validation'].idxmax()]

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# So we determined best estimator at $k = 4$:
# - Fit the full train set with estimator at this value of $k$.
# - Evaluate performance on true test/hold-out.

# %% slideshow={"slide_type": "fragment"}
fulltrain_scaler = StandardScaler()
X_train_sc = fulltrain_scaler.fit_transform(X_train)
X_test_sc = fulltrain_scaler.transform(X_test)

best_estimator = KNeighborsClassifier(n_neighbors = 4)
best_estimator.fit(X_train_sc, y_train)

# get predictions
y_pred = best_estimator.predict(X_test_sc)

# %% slideshow={"slide_type": "slide"}
from sklearn.metrics import plot_confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import classification_report

# %% cell_style="center" slideshow={"slide_type": "fragment"}
#plot_confusion_matrix(best_estimator, X_test_sc, y_test);
ConfusionMatrixDisplay.from_estimator(best_estimator, X_test_sc, y_test);

# %% slideshow={"slide_type": "fragment"}
print(classification_report(y_test, y_pred))

# %% [markdown] slideshow={"slide_type": "slide"}
# In 2D feature space: 
# - visualize decision boundary
# - prediction space vs. actual data

# %% slideshow={"slide_type": "slide"}
X_full_sc = fulltrain_scaler.transform(X)
x_min, x_max = X_full_sc[:, 0].min() - 1, X_full_sc[:, 0].max() + 1
y_min, y_max = X_full_sc[:, 1].min() - 1, X_full_sc[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))

f, ax = plt.subplots()

Z = best_estimator.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
ax.contourf(xx, yy, Z, alpha=0.4)
ax.scatter(X_full_sc[:, 0], X_full_sc[:, 1], c = y, s=30, edgecolor="k")
ax.set_xlabel('Sepal width [scaled]')
ax.set_ylabel('Petal width [scaled]')
ax.set_title('Decision Boundary: KNN (k = 4)')
plt.show()

# %% [markdown] slideshow={"slide_type": "slide"}
# This is pretty decent and not too bad on the overfitting:
# - Given small dataset size
# - Some irregularities in decision boundary 
# - Validation score as a function of $k$
#     - Consider increasing $k$ a little.

# %% [markdown] slideshow={"slide_type": "slide"}
# #### The effectiveness of the KNN classifier

# %% [markdown] cell_style="split" slideshow={"slide_type": "fragment"}
# - Naturally learns complex boundaries.
# - KNN can be prone to overfitting
#

# %% [markdown] cell_style="split" slideshow={"slide_type": "fragment"}
# **Another less obvious point:**
# - Performance scales badly as the number of features get big
#

# %% [markdown] slideshow={"slide_type": "fragment"}
# Let's see why

# %% [markdown] slideshow={"slide_type": "slide"}
# Take points in 2D:

# %% [markdown] slideshow={"slide_type": "fragment"}
# <img src = "Images/1dto2D_CoD.gif" width = 500/>
# <center> Same number of points denser in 1D. </center>

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# Extend 2D to 3D:
# - Number of points fixed
# - Random z-position selection within the cube
#

# %% [markdown] cell_style="split" slideshow={"slide_type": "fragment"}
# <img src = "Images/2dto3d_CoD.gif" width = 500/>
# <center> The density now?</center>

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# Extend 3D to 4D (add time dimension):
# - Snapshots = 3D cross-section of 4D-cube.
#
# Visualize from 1D to 4D.

# %% [markdown] cell_style="split" slideshow={"slide_type": "fragment"}
# <img src = "Images/CoD.gif" />

# %% [markdown] cell_style="center" slideshow={"slide_type": "fragment"}
# As my dimensionality increases:
#
# - Neighbors get sparse.
# - volume scales **exponentially** with number of features.

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# Being more systematic:
#
# Volume of sphere in $M$ dimensions:
#
# $$ V_M(R) = \frac{\pi^{M/2}}{\Gamma(\frac{M}{2} + 1)}R^M $$

# %% cell_style="center" slideshow={"slide_type": "fragment"}
from scipy.special import gamma

def sphere_calc(m, R):
    numerator = (R**m * np.pi**(m/2))
    denom = gamma(m/2 + 1)
    
    return numerator/denom

dim_list = pd.Series(np.arange(1,21))
sph_vol_list = dim_list.map(lambda M: sphere_calc(M, 2)) # get +- 2 std of standardized variables

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# Now if I have moderate sized dataset of $N = 5000$ points:
# - After variable standardization: ~ $\pm 2 \sigma$
# - Sphere of radius 2.
# - Let's see how the density scales: $$ \rho = \frac{N}{V_M(2)} $$

# %% cell_style="split" slideshow={"slide_type": "slide"}
density_vs_dim = 5000/sph_vol_list
fig, ax = plt.subplots()
sns.lineplot(x = density_vs_dim.index, y = density_vs_dim.values, ax = ax)
ax.set_ylabel('Point density')
ax.set_xlabel('Number of Features')
ax.set_title('Point density:  feature dimension scaling')
plt.show()

# %% [markdown] cell_style="split" slideshow={"slide_type": "fragment"}
# Life is a lonely place at high dimension:
# - Unlikely to have a neighbor within a unit sphere at moderate to high dimensions
#

# %% cell_style="split" slideshow={"slide_type": "fragment"}
density_vs_dim.head(10)

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# This affects all algorithms in small to mid-size problems:
# - Need good statistical sampling in feature space for training
# - Dataset become sparse in high dimension. Hard to do statistical learning.

# %% [markdown] slideshow={"slide_type": "fragment"}
# **Local, distance based algorithms are especially affected by high D**
# - Classification built off point-by-point local consideration.
# - Nearest neighbors of a given point: very far away in feature space.
# - For each point: unreasonable to rely on tyranny of neighbors.
#
# Majority voting with KNN: starts to be a bad idea.

# %% [markdown] slideshow={"slide_type": "slide"}
# **Solution**: Dimensionality reduction techniques (will talk about later).

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# # Level Up: Distance Metrics
# > The "closeness" of data points → proxy for similarity

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](./images/distance.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# - Minkowski: $dist(A,B) = (\sum_{k=1}^{N} |a_k - b_k|^c)^\frac{1}{c} $$
#
#
#
# - Manhattan: $dist(A,B) = \sum_{k=1}^{N} |a_k - b_k|$
#
#
#
# - Euclidean: $dist(A,B) = \sqrt{ \sum_{k=1}^{N} (a_k - b_k)^2 }$

# %% [markdown] slideshow={"slide_type": "fragment"}
# There are quite a few different distance metrics built-in for Scikit-learn: 
#
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DistanceMetric.html?highlight=distance#sklearn.metrics.DistanceMetric

# %% [markdown]
# Pros and cons of distance metrics:
#
# https://towardsdatascience.com/9-distance-measures-in-data-science-918109d069fa

# %%
