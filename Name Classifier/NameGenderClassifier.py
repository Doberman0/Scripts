#Name classifier - classifies names by their "gender"
from nltk.corpus import names #Getting the corpus/set of info
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
import random

def gender_features(name):
    '''
    Note that too many features lend to overfitting...
    
    features = {}
    features['first_letter'] = name[0].lower()
    features['last_letter'] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features['count({})'.format(letter)] = name.lower().count(letter)
        features['has({})'.format(letter)] = (letter in name.lower())
    return features #returns a feature set
    '''
    return {'suffix1': name[-1:],
            'suffix2': name[-2],
            'last_letter': name[-1]}

def whatGenderIsThisName(name): #Returns the gender of the name you enter
    return classifier.classify(gender_features(name))

def classifierAccuracy(): #Returns how accurate the classifier is thus far
    print(nltk.classify.accuracy(classifier, test_set))

def mostInformativeFeatures(): #Returns the top 10 most informative features
    return classifier.show_most_informative_features(10)

def findErrors():
    errors = []
    for (name, tag) in devtest_names:
        guess = classifier.classify(gender_features(name))
        if guess != tag:
            errors.append((tag, guess, name))
    for (tag, guess, name) in sorted(errors):
        print('correct = {:<8} guess = {:<8s} name = {:<30}'. format(tag, guess, name))
        

if __name__ == '__main__':
    #Import data
    labelled_names = ([(name, 'male') for name in names.words('male.txt')] +
                      [(name, 'female') for name in names.words('female.txt')])

    #Randomly rearrange tuples
    random.shuffle(labelled_names)

    #Building training and test data
    featuresets = [(gender_features(name), gender) for (name, gender) in labelled_names]
    train_set, dev_set, test_set = featuresets[1500:], featuresets[500:1500],featuresets[:500]
    classifier = nltk.NaiveBayesClassifier.train(train_set)

    #Using devtest_names for error analysis
    train_names, devtest_names, test_names = labelled_names[1500:], labelled_names[500:1500], labelled_names[:500]


