from Guest.models import Inventory
from django.db.models import Count
from plotly.offline import plot
from plotly.graph_objs import Bar
from plotly.graph_objects import Layout
from plotly.graph_objects import Figure
def creatPlotly(label,xtitle,ytitle,plot_title):
    results = Inventory.objects.values(label).annotate(dcount=Count("quantity"))
    x = []
    y = []
    for i,result in zip(range(len(results)),results):
        r = list(result.values())
        x.append(r[0])
        y.append(r[1])
    trace = Bar(x=x, y=y,name='Prestige Smart Analysis',
                        opacity=0.8, marker_color='green')
    data = [trace]
    layout = Layout(
        title=plot_title,
        xaxis=dict(
            title=xtitle,
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        ),
        yaxis=dict(
            title=ytitle,
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )
    fig = Figure(data=data, layout=layout)
    return plot(fig,output_type="div")
