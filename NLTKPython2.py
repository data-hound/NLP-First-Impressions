import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle

from sklearn.naive_bayes import MultinomialNB, BernoulliNB, GaussianNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

from nltk.classify import ClassifierI
#from statistics import mode

class VoteClassifier(ClassifierI):
	def __init__(self, *classifiers):
		self._classifiers = classifiers

	def classify(self, features):
		votes = []
		for c in self._classifiers:
			v=c.classify(features)
			votes.append(v)
		return mode(votes)

	def confidence(self,features):
		votes = []
		for c in self._classifiers:
			v=c.classify(features)
			votes.append(v)
		choice_votes = votes.count(mode(votes))
		conf = choice_votes/len(votes)
		return conf

documents = [(list(movie_reviews.words(fileid)),category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)


all_words = []

for w in movie_reviews.words():
	all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:3000] 

def find_features(document):
	words = set(document)
	features = {}
	for w in word_features:
		features[w] = {w in words}
	
	return features

featuresets = {find_features(rev, category) for (rev, category) in documents}

training_set = featuresets[:1900]
testing_set = featurs[1900:]

classifier_f = open('naivebayes.pickle','rb')
classifier = pickle.load(classifier_f)
classifier_f.close()

print 'Naive Bayes Algo acuracy percent:',(nltk.classify.accuracy(classifier, training_set)*100),classifier.show_most_informative_features(15)
 

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print "MNB_classidier accuracy percent:", nltk.classify.accuracy(MNB_classifier, training_set)*100, classifier.show_most_informative_features(15)

BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print "BernoulliNB_classidier accuracy percent:", nltk.classify.accuracy(BernoulliNB_classifier, training_set)*100, classifier.show_most_informative_features(15)

GaussianNB_classifier = SklearnClassifier(GaussianNB())
GaussianNB_classifier.train(training_set)
print "GaussianNB_classidier accuracy percent:", nltk.classify.accuracy(GaussianNB_classifier, training_set)*100, classifier.show_most_informative_features(15)

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print "LogisticRegression_classidier accuracy percent:", nltk.classify.accuracy(LogisticRegression_classifier, training_set)*100, classifier.show_most_informative_features(15)

SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(training_set)
print "SVC_classidier accuracy percent:", nltk.classify.accuracy(SVC_classifier, training_set)*100, classifier.show_most_informative_features(15)

SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print "SGDClassifier_classidier accuracy percent:", nltk.classify.accuracy(SGDClassifier_classifier, training_set)*100, classifier.show_most_informative_features(15)

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print "LinearSVC_classidier accuracy percent:", nltk.classify.accuracy(LinearSVC_classifier, training_set)*100, classifier.show_most_informative_features(15)

NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print "NuSVC_classidier accuracy percent:", nltk.classify.accuracy(NuSVC_classifier, training_set)*100, classifier.show_most_informative_features(15)

#voted_classifier = VoteClassifier(classifier, MNB_classifier)

#print "Voted_classifier accuracy percent:", nltk.classify.accuracy(MNB_classifier, training_set)*100, classifier.show_most_informative_features(15)


