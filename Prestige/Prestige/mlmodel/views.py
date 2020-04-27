from django.shortcuts import render
from Guest.models import Reviews
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy
from plotly.offline import plot
from plotly.graph_objs import Bar 
import nltk
nltk.download('movie_reviews')


def extract_features(words):
    return dict([(word, True) for word in words])

#import nltk
#nltk.download('movie_reviews')

def SentimentAnalyzer(text):
    # load movie reviews from sample data
    fileids_pos = movie_reviews.fileids('pos')
    fileids_neg = movie_reviews.fileids('neg')

    features_pos = [(extract_features(movie_reviews.words(fileids=[f])),'Positive') for f in fileids_pos]
    features_neg = [(extract_features(movie_reviews.words(fileids=[f])),'Negative') for f in fileids_neg]

    threshold = 0.8
    num_pos = int(threshold*len(features_pos))
    num_neg = int(threshold*len(features_neg))

    # creating training and testing data
    features_train = features_pos[:num_pos] + features_neg[:num_neg]
    features_test = features_pos[num_pos:] + features_neg[num_neg:]

    #print('\nNumber of training datapoints:', len(features_train))
    #print('Number of test datapoints:', len(features_test))

    # training a naive bayes classifier 
    classifier = NaiveBayesClassifier.train(features_train)
    print('Accuracy:',nltk_accuracy(classifier, features_test))

    probabilities = classifier.prob_classify(extract_features(text.split()))
    # Pick the maximum value
    predicted_sentiment = probabilities.max()
    print("Predicted sentiment:", predicted_sentiment)
    print("Probability:",round(probabilities.prob(predicted_sentiment), 2))

    return predicted_sentiment  
# SentimentAnalyzer('It was not that good.')

def modelResults(request):
    reviews = Reviews.objects.all()
    results = []
    for review in reviews:
        results.append(SentimentAnalyzer(review))
    x = ['Positive,Negative']
    plot_div = plot([Bar(x=x, y=results,
                        name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    return render(request, "model.html", context={'plot_div': plot_div})

    
    
    

