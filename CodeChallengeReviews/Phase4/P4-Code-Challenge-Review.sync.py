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

# %% [markdown] index=0
# # Phase 4 Code Challenge Review
#
# Made using resources that Max put together, thanks Max!

# %% [markdown]
# ## Overview
#
# - Principal Component Analysis
# - Clustering
# - Time Series
# - Natural Language Processing

# %%
# Basic Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
# from src.call import call_on_students

# %% [markdown]
# # 1) Principal Component Analysis
#
# ![pca gif saved from learnco](images/pca.gif)

# %% [markdown]
# ## PCA Concepts

# %% [markdown]
# ### 1: What does PCA do? 
#
# Specifically, describe what the first principal component represents in relation to the original data.

# %%
# call_on_students(1)

# %% [markdown]
# #### Answer: 
#
# - A dense matrix, where the dimensionality of the original data has been reduced by collapsing some
#   dimensions, along one or more orthogonal axes.
#

# %% [markdown]
# ### 2: What are some reasons to use PCA?

# %%
# call_on_students(1)

# %% [markdown]
# #### Answer: 
#
# - To reduce calculation time.
#

# %% [markdown]
# ### 3: Why is scaling important for PCA?

# %%
# call_on_students(1)

# %% [markdown]
# #### Answer: 
#
# - Because if there is a difference in scale between feature dimensions then thier relationship 
#   will be distorted by collapsing the orthogonal distance between them.
#

# %% [markdown]
# ### 4: How can one determine how many principle components to use in a model?

# %%
# call_on_students(1)

# %% [markdown]
# #### Answer: 
#
# - I don't know
#

# %% [markdown] index=16
# ## PCA in Code
#
# ### Set Up

# %% index=17
from sklearn.datasets import  load_breast_cancer

data = load_breast_cancer()
X = pd.DataFrame(data['data'], columns = data['feature_names'])
X.head()

# %% [markdown]
# ### 5: Prepare our Data for PCA
#
# What steps do we need to take to preprocess our data effectively?
#
# - scale it. 
#

# %%
# call_on_students(1)

# %% index=18
# Code to preprocess X
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_X = scaler.fit_transform(X)

# %% [markdown]
# ### 6: Import PCA, Then Instantiate and Fit a PCA Object

# %%
# call_on_students(1)

# %% index=19
# Code to import, instantiate and fit a PCA object
from sklearn.decomposition import PCA
pca = PCA(n_components=2)

pca_X = pca.fit_transform(X)

# %% [markdown]
# ### 7: How Much Variance is Explained by the First 2 Components?

# %%
# call_on_students(1)

# %% index=20
# Code here to answer the question
pca.explained_variance_ratio_

# %% [markdown]
# #### Answer:
#
# - the first feature explains almost all of the variance in the data
#

# %% [markdown] index=83
# # 2) Clustering

# %% [markdown]
# ## Clustering Concepts

# %% [markdown]
# ### 8: Describe how the K-Means algorithm updates its cluster centers after initialization.

# %%
# call_on_students(1)

# %% [markdown]
# #### Answer:
#
# - It measures the amount of inertia at each step and looks for the difference to level out. 
#

# %% [markdown]
# ### 9: What is inertia, and how does K-Means use inertia to determine the best estimator?
#
# Please also describe the method you can use to evaluate clustering using inertia.
#
# Documentation, for reference: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

# %%
# call_on_students(1)

# %% [markdown]
# #### Answer:
#
# - 
#

# %% [markdown]
# ### 10: What other metric do we have to score the clusters which are formed?
#
# Describe the difference between it and inertia.

# %%
# call_on_students(1)

# %% [markdown]
# #### Answer:
#
# - 
#

# %% [markdown] index=95
# ## Clustering in Code with Heirarchical Agglomerative Clustering

# %% [markdown] index=96
# After the above conceptual review of KMeans, let's practice coding with agglomerative clustering.
#
#
# ### Set Up

# %% index=97
# New dataset for this section!
from sklearn.datasets import load_iris

data = load_iris()
X = pd.DataFrame(data['data'])

# %% [markdown]
# ### 11: Prepare our Data for Clustering
#
# What steps do we need to take to preprocess our data effectively?
#
# - 
#

# %%
# call_on_students(1)

# %% index=99
# Code to preprocess the data
# Name the processed data X_processed
X_processed = None


# %% [markdown]
# ### 12: Import the Relevant Class, Then Instantiate and Fit a Hierarchical Agglomerative Clustering Object
#
# Let's use `n_clusters = 2` to start (default)

# %%
# call_on_students(1)

# %%
# Import the relevent clustering algorithm

# %% index=100
# Fit the object

# %% index=101
# Calculate a silhouette score

# %% [markdown]
# ### 13: Write a Function to Test Different Options for `n_clusters`
#
# The function should take in the number for `n_clusters` and the data to cluster, fit a new clustering model using that parameter to the data, print the silhouette score, then return the labels attribute from the fit clustering model.

# %%
# call_on_students(1)

# %%
def test_n_for_clustering(n, data):
    """ 
    Tests different numbers for the hyperparameter n_clusters
    Prints the silhouette score for that clustering model
    Returns the labels that are output from the clustering model

    Parameters: 
    -----------
    n: float object
        number of clusters to use in the agglomerative clustering model
    data: Pandas DataFrame or array-like object
        Data to cluster

    Returns: 
    --------
    labels: array-like object
        Labels attribute from the clustering model
    """
    # Fit the new clustering model
    
    # Print the silhouette score
    
    # Return the labels attribute from the fit clustering model
    
    pass


# %%
# Testing your function

for n in range(2, 9):
    test_n_for_clustering(n, X_processed)

# %% [markdown] index=51
# # 3) Time Series

# %% index=52
# New dataset for this section!
ap = pd.read_csv('data/AirPassengers.csv')
ap.head()

# %% [markdown]
# ### 14: Prepare our Data for Time Series Analysis
#
# What steps do we need to take to preprocess our data effectively?
#
# - 
#

# %%
# call_on_students(1)

# %%
# Code here 

# %% [markdown]
# ### 15: Explore Patterns in the Data

# %%
# call_on_students(1)

# %% [markdown]
# First: what kinds of patterns can one find in time series data?
#
# - 
#

# %% [markdown]
# Second, plot this time series data. What kinds of patterns do you see in this dataset?

# %% index=62
# Code to plot the time series

# %% [markdown]
# ### 16: Explore the Moving Average
#
# What window would make sense to use for this data?
#
# - 
#

# %%
# call_on_students(1)

# %%
# Code to create the moving average

# %% index=67
# Add to the moving average to the above plot

# %% [markdown]
# ### 17: Explore Stationarity
#

# %%
# call_on_students(1)

# %% [markdown] index=69
# Why do we try to make our data stationary?
#
# - 
#

# %% [markdown] index=69
# What can we do to make our data stationary?
#
# - 
#

# %% [markdown]
# ### 18: Check Stationarity

# %%
# call_on_students(1)

# %% index=80
# Code here to check if the data is stationary

# %% [markdown]
# ### 19: Try to Make the Data Stationarity
#
# Implement one strategy to try to make the data more stationary, then check if it worked.

# %%
# call_on_students(1)

# %% index=73
# Code here to try to make the data stationary

# %%
# Code here to check if the data is stationary

# %% [markdown] index=82
# <a id='clust'></a>

# %% [markdown] index=23
# # 4) Natural Language Processing

# %% [markdown]
# ## NLP Concepts
#
# ### Some Example Text

# %% index=24
# Each sentence is a document
sentence_one = "Harry Potter is the best young adult book about wizards"
sentence_two = "Um, EXCUSE ME! Ever heard of Earth Sea?"
sentence_three = "I only like to read non-fiction.  It makes me a better person."

# The corpus is composed of all of the documents
corpus = [sentence_one, sentence_two, sentence_three]

# %% [markdown]
# ### 20: NLP Pre-processing
#
# List at least three steps you can take to turn raw text like this into something that would be semantically valuable (aka ready to turn into numbers):

# %%
# call_on_students(1)

# %% [markdown] index=25
# #### Answer:
#
# 1.  
# 2. 
# 3. 

# %% [markdown]
# ### 21: Describe what vectorized text would look like as a dataframe.
#
# If you vectorize the above corpus, what would the rows and columns be in the resulting dataframe (aka document term matrix)

# %%
# call_on_students(1)

# %% [markdown] index=25
# #### Answer:
#
# - 
#

# %% [markdown]
# ### 22: What does TF-IDF do?
#
# Also, what does TF-IDF stand for?

# %%
# call_on_students(1)

# %% [markdown] index=25
# #### Answer:
#
# - 
#

# %% [markdown] index=33
# ## NLP in Code
#
# ### Set Up

# %% index=34
# New section, new data
policies = pd.read_csv('data/2020_policies_feb_24.csv')

def warren_not_warren(label):
    
    '''Make label a binary between Elizabeth Warren
    speeches and speeches from all other candidates'''
    
    if label =='warren':
        return 1
    else:
        return 0
    
policies['candidate'] = policies['candidate'].apply(warren_not_warren)

# %% [markdown] index=35
# The dataframe loaded above consists of policies of 2020 Democratic presidential hopefuls. The `policy` column holds text describing the policies themselves.  The `candidate` column indicates whether it was or was not an Elizabeth Warren policy.

# %% index=36
policies.head()

# %% [markdown] index=37
# The documents for activity are in the `policy` column, and the target is candidate. 

# %% [markdown]
# ### 23: Import the Relevant Class, Then Instantiate and Fit a Count Vectorizer Object

# %%
# call_on_students(1)

# %%
# First! Train-test split the dataset
from sklearn.model_selection import train_test_split

# Code here to train test split

# %%
# Import the relevant vectorizer

# %%
# Instantiate it

# %%
# Fit it

# %% [markdown]
# ### 24: Vectorize Your Text, Then Model

# %%
# call_on_students(1)

# %% index=42
# Code here to transform train and test sets with the vectorizer

# %% index=44
# Importing the classifier...
from sklearn.ensemble import RandomForestClassifier

# Code here to instantiate and fit a Random Forest model


# %%
# Code here to evaluate your model on the test set
