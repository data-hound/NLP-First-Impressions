import nltk
import os
import nltk.corpus as corpora
from nltk.tokenize import PunktSentenceTokenizer
import random
import pylab as PL
import matplotlib.pyplot as plt
import csv
import pandas as pd


Gutenberg = corpora.gutenberg #fileids()
WebTxt = corpora.webtext #fileids()
Brown = corpora.brown #categories()
Dictionary = corpora.words

vocab = Dictionary.words('en')

#This is a dictionary used to store the symbol distribution
#Each key in the dictionary is a symbol 
#Value corresponding to each key is a list of size 100
#At any given key, the value of the key gives the distribution of the symbol in the text processed
symb_dist = dict()



'''This Function is used to set the symb_dist dictionary for a new word
   Each new word is processed to obtain the relative positions of the symbols in the word
   The corresponding position in the value(a list of distribution) is incremented for the respective key(symbol)'''
def set_dict(word):
    word=word.lower()
    length = len(word)
    #symb_dist['a']=[0]*100

    for i in range(0,length):
        #print word[i],
        #symbol=symb_dist[str(word[i])]
        rel_pos= int(round((i/float(length))*100))
        #print symb_dist['a']

        if word[i] in symb_dist.keys():
            symb_dist[str(word[i])][rel_pos]+=1
        else:
            symb_dist[str(word[i])]=[0]*100
            symb_dist[str(word[i])][rel_pos]+=1
        
    #print ''

'''Set the symb_dist for a given word file and write the output to a csv file'''
def init():   
    #In this loop we are Setting up the symb_dist for a given document
    for i in vocab:
        if len(i)==1:# and i in ('a','z'):
            print i
        #print i
        set_dict(i)

    #In this loop we are normalizing the values in the lists corresponding to keys
    for j in symb_dist.keys():
        tot=sum(symb_dist[j])
        symb_dist[j][:] = ((100*x/float(tot)) for x in symb_dist[j])

    keys = sorted(symb_dist.keys())
    
    
    sub_dir = "Dictionary"
    
    try:
        os.mkdir(sub_dir)
    except Exception:
        pass
    

    with open(os.path.join(sub_dir,"symb_dist"+".csv"), "wb") as outfile:
        writer = csv.writer(outfile, delimiter = "\t")
        writer.writerow(keys)
        writer.writerows(zip(*[symb_dist[key] for key in keys]))

    colors=['r','g','b','k']
    count = 0

    for k in symb_dist.keys():
        plt.figure(count)
        plt.plot(symb_dist[k],colors[count%4])                         #Plotting the symbol distribution
        plt.savefig(os.path.join(sub_dir,k+".png"))                    #Saving the plots
        count+=1
    #plt.show()
    

def get_path():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print dir_path
    cwd = os.getcwd()
    print cwd

get_path()
init()
