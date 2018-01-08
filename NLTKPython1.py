##import nltk
##
###nltk.download()
##
##from nltk.tokenize import sent_tokenize, word_tokenize
##
##example_text='Hello Mr. Smith(there), how are you doing today? The'
######print(sent_tokenize(example_text))
######print(word_tokenize(example_text))
##
##
##from nltk.corpus import stopwords
##from nltk.tokenize import word_tokenize
##
##example='This is an example showing the use of stop words'
##stop_words= set(stopwords.words("english"))
##
##words=word_tokenize(example)
##
##filtered_sentence= []
##
##for w in words:
##    if w not in stop_words:
##        filtered_sentence.append(w)
##
##print filtered_sentence


import nltk
from nltk.corpus import movie_reviews
from nltk.tokenize import PunktSentenceTokenizer
import random

'''sample_text = state_union.raw('2005-GWBush.txt')
train_text = state_union.raw('2004-GWBush.txt')

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print tagged
        

    except Exception as e:
        print str(e)

process_content()'''

documents=[(list(movie_reviews.words(fileid)),category)
           for category in movie_reviews.categories()
           for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words= []

for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

#Thers a huge ammount of words in these all_words, there may be words that are not needed
#top 3000 words will encompass most of the common words that we can use to train a classifier

word_features = list(all_words.keys())[:3000]

#We define a function to find those features within the document we are usingg


def find_features(document):
    words= set(documents)#documents are going to be lists of words
    #When we convert a list into a set we basically get a single occurence for each element in list

    features={}#empty dictionary

    for w in word_features:
        features[w]={w in words}#=>if one of these top 3000 words is in this document, it wil return true

    return features

#print find_features(movie_reviews.words('neg/cv000_29416.txt'))

featuresets=[(find_features(rev),category) for (rev,category) in documents]
#we are converting the data, each document is going to be just the reviews, and word and the category
#we convert that to not a review but a dictionary of top 3000 words and whether or not its present in a document

training_set= featuresets[:1900]
testing_set=featuresets[1900:]

########****NAIVE BAYES****##################
# posterior = prior
#It is very scalable

classifier = nltk.NaiveBayesClassifier.train(training_set)
print 'Naive Bayes Algo Accuracy percent',(nltk.classify.accuracy(classifier,testing_set)*100)

classifier.show_most_informative_features(15)


