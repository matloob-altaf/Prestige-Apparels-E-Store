from django.shortcuts import render
from Guest.models import Reviews
from plotly.offline import plot
from plotly.graph_objs import Bar
from mlmodel.ml import SentimentAnalyzer





def modelResults(request):
    reviews = Reviews.objects.all().values_list('comments')
    #reviews = ['Very Nice','Very Beauttiful']
    texts = []
    for review,i in zip(reviews,range(len(reviews))):
        texts.append(review[0][i])

    results = SentimentAnalyzer(texts)
    sum_positive = 0
    sum_negative = 0
    for result in results:
        if result=='Positive':
            sum_positive = sum_positive+1
        else:
            sum_negative = sum_negative+1
    y_data = [sum_positive,sum_negative]
    x_data = ['Positive','Negative']
    plot_div = plot([Bar(x=x_data, y=y_data,
                            name='Prestige Product Sizes',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    return render(request, "model.html", context={'plot_div': plot_div})

    

    
    
    

