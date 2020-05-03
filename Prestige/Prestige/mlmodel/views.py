from django.shortcuts import render
from Guest.models import Reviews
from plotly.offline import plot
from plotly.graph_objs import Bar
from mlmodel.ml import SentimentAnalyzer


def modelResults(request):
    '''function to perform sentiment analysis of comments on the website using a
    machine learning classifier which uses proabilistic method to classify 
    comments and plot the results using a fancy plotly graph. The classifier
    is trained on roman urdu dataset as the audience of our app is Pakistani
    People who frequently uses roman urdu in day to day arguments'''
    reviews = Reviews.objects.all().values_list('comments') #Fetching comments
    #reviews = ['Very Nice','Very Beauttiful'] #Pseudo reviews used for testing 
    texts = []
    #Creating a list of comments
    for review,i in zip(reviews,range(len(reviews))):
        texts.append(review[0][i])
    #Passing the result to the sentiment analyzer function 
    results = SentimentAnalyzer(texts)
    #Summing the positive and negative comments
    sum_positive = 0
    sum_negative = 0
    for result in results:
        if result=='Positive':
            sum_positive = sum_positive+1
        else:
            sum_negative = sum_negative+1
    #Adding the data to be plotted on x and y axis and passing it to the plotting function and page
    y_data = [sum_positive,sum_negative]
    x_data = ['Positive','Negative']
    plot_div = plot([Bar(x=x_data, y=y_data,
                            name='Prestige Product Sizes',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    return render(request, "model.html", context={'plot_div': plot_div})

    

    
    
    

