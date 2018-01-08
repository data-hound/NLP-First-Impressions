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

def get_comparisons():
    cluster_dict = dict()
    file_open = open('output_file1.txt','rb')
    count = 0
    file2list = list()

    for line in file_open:
        #print type(line)
        line_ = line.strip()
        cluster_dict[vocab[count]] = vocab[int(line_)]
        count+=1

    
    print cluster_dict
    print len(cluster_dict)
    
    file_open.close()
    
    
get_comparisons()
