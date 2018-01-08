import nltk
import random
import matplotlib
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)),category)
              for category in movie_reviews.categories()
              for fileid in movie_reviews.fileids(category)]

#same as:
'''
documents=[]
for category in movie_reviews.categories():
        for fileid in movie_reviews.fileids(category):
            documents.append(movie_revies.words(fileids),categories)
'''

random.shuffle(documents)#to mess with the order so that we can get test and train data easily

#print documents[1]

all_words=[]

for w in movie_reviews.words():
    all_words.append(w.lower())# We put convert words into lowe case and append them to all_words

all_words=nltk.FreqDist(all_words)
all_words.plot()
