from django.shortcuts import render
from Guest.models import Reviews
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy
from plotly.offline import plot
from plotly.graph_objs import Scatter,Bar
from mlmodel.ml import SentimentAnalyzer


def modelResults(request):
    reviews = Reviews.objects.all().values_list('comments')
    results = []
    for review in reviews:
        results.append(SentimentAnalyzer(review))
    y_data = results
    x_data = ['Positive','Negative']
    plot_div = plot([Bar(x=x_data, y=y_data,
                            name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    return render(request, "model.html", context={'plot_div': plot_div})

    

    
    
    

