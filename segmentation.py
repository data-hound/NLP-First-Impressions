import nltk
import os
import subprocess
import math
import nltk.corpus as corpora
from nltk.tokenize import PunktSentenceTokenizer
import random
import pylab as PL
import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
import sklearn
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import AffinityPropagation

Gutenberg = corpora.gutenberg #fileids()
WebTxt = corpora.webtext #fileids()
Brown = corpora.brown #categories()
Dictionary = corpora.words
#dbscan = sklearn.cluster.DBSCAN
#kmeans = sklearn.cluster.KMeans

vocab = Dictionary.words('en')

#This is a dictionary used to store the symbol distribution
#Each key in the dictionary is a symbol 
#Value corresponding to each key is a list of size 100
#At any given key, the value of the key gives the distribution of the symbol in the text processed
symb_dist = dict()


def clust():
    file_path = os.getcwd()+"/A/vec_dict.csv"
    print file_path
    
    dict_df = pd.read_csv(file_path, usecols= []+range(2,28))
    #word_labels = list(dict_df.index)
    
    dict_df_2 = pd.read_csv(file_path)
    word_labels = dict_df_2.ix[:,0].tolist()
    #print type(dict_df)
    #print dict_df
    
    np_matrix = dict_df.as_matrix()
    #print np_matrix
    #print type(np_matrix)
    
    X = list()
    for i in np_matrix:
        sq_sum = 0.0
        for j in i:
            sq_sum = sq_sum + j**2
        root_sq_sum = math.sqrt(sq_sum)
        X.append(i/root_sq_sum)
    
    X = np.array(X)
            
    print X[0:3]
    print type(X)
    Y = word_labels
    
    
    
    #Some variable definitions for cluster numbers
    curr_clusters = len(Y)/3;
    #print Y
    
    
    #--------------------K-MEANS-------------------------
    #K-means runs extremely slowly and has memory overflow
    #k_means = KMeans(n_clusters = curr_clusters).fit(X)
    #roots = k_means.cluster_centers_
    
    
    #---------------DBSCAN CLUSTERING--------------------------
    #This clustering has produced results in reasonable time
    #print roots
    #_eps = 0.3
    #min_derivs = 3
    #db = DBSCAN(eps = _eps, min_samples = min_derivs).fit(X)
    #labels_ = db.labels_
    
    
    
    #-------------AGGLOMERATIVE CLUSTERING---------------------
    #Gives memory error, possibly due to double datatype
    #agc = AgglomerativeClustering(n_clusters=curr_clusters, affinity='cosine', linkage= 'complete')
    #agc.fit(X)
    #labels_ = agc.labels_
    
    #-------------------AFFINITY PROPAGATION----------------------
    #Memory Error again
    #af = AffinityPropagation(preference=-50).fit(X)
    #cluster_centers_indices = af.cluster_centers_indices_
    #labels_ = af.labels_
    
    #-----------------MINI BATCH K-MEANS----------------------------
    km = MiniBatchKMeans(n_clusters=curr_clusters, init='k-means++', n_init=1,
                         init_size=1000, batch_size=1000)
    km.fit(X)
    labels_ = km.labels_
    print labels_.shape
    
    op_file = open('output_file1.txt','w')
    for item in labels_:
        op_file.write("%s \n" % item)
    
        
clust()
