#from nltk.corpus import movie_reviews
#from nltk.classify.util import accuracy as nltk_accuracy
import pickle 




#import nltk
#nltk.download('movie_reviews')


# def save_classifier(classifier):
#    f = open('my_classifier.pickle', 'wb')
#    pickle.dump(classifier, f, -1)
#    f.close()
#    print("Saved the classifier")

def load_classifier():
   f = open('my_classifier.pickle', 'rb')
   classifier = pickle.load(f)
   f.close()
   return classifier

def SentimentAnalyzer(text):
    # load movie reviews from sample data
    # fileids_pos = movie_reviews.fileids('pos')
    # fileids_neg = movie_reviews.fileids('neg')

    # features_pos = [(extract_features(movie_reviews.words(fileids=[f])),'Positive') for f in fileids_pos]
    # features_neg = [(extract_features(movie_reviews.words(fileids=[f])),'Negative') for f in fileids_neg]

    #threshold = 0.8
    # num_pos = int(threshold*len(features_pos))
    # num_neg = int(threshold*len(features_neg))

    # # creating training and testing data
    # features_train = features_pos[:num_pos] + features_neg[:num_neg]
    # features_test = features_pos[num_pos:] + features_neg[num_neg:]

    #print('\nNumber of training datapoints:', len(features_train))
    #print('Number of test datapoints:', len(features_test))

    # training a naive bayes classifier 
    classifier = load_classifier()
    #print('Accuracy:',nltk_accuracy(classifier, features_test))
    results = list(classifier.predict(text))
    return results  
# SentimentAnalyzer('It was not that good.')