from django.shortcuts import render
from django.http import HttpResponse
from ..api.fusioncharts import FusionCharts
from ..models import *


# The `chart` function is defined to generate Column 2D chart from database.
def graph(request, id):
    # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
    # dataSource = {}
    #
    # dataSource['chart'] = {
    #     "caption": "Monthly revenue for last year",
    #     "subCaption": "Harry's SuperMart",
    #     "xAxisName": "Month",
    #     "yAxisName": "Revenues (In USD)",
    #     "numberPrefix": "$",
    #     "theme": "zune"
    # }
    #
    # # The data for the chart should be in an array where each element of the array is a JSON object
    # # having the `label` and `value` as key value pair.
    #
    # dataSource['data'] = []
    # # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    # for key in Revenue.objects.all():
    #     data = {}
    #     data['label'] = key.Month
    #     data['value'] = key.MonthlyRevenue
    #     dataSource['data'].append(data)
    #
    #     # Create an object for the Column 2D chart using the FusionCharts class constructor
    # column2D = FusionCharts("column2D", "ex1", "600", "350", "chart-1", "json", dataSource)
    # return render(request, 'index.html', {'output': column2D.render()})
    
    print(id)
    return render(request, "index.html")