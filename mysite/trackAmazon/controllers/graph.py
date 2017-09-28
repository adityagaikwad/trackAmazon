from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..api.fusioncharts import FusionCharts
from ..models import *


# The `chart` function is defined to generate Column 2D chart from database.
def graph(request, id):
    if "email" in request.session:
        # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
        dataSource = {}
        product = Product.objects.get(product_id=id)
        dataSource['chart'] = {
            "caption": "Price Trends for "+ str(product.title),
            "subCaption": "",
            "xAxisName": "Date",
            "yAxisName": "Cost (in Rupees)",
            "numberPrefix": "",
            "theme": "zune"
        }
    
        # The data for the chart should be in an array where each element of the array is a JSON object
        # having the `label` and `value` as key value pair.
    
        dataSource['data'] = []
        # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
        for key in Graph.objects.filter(product_id=id):
            # product = Product.objects.get(product_id=id)
            data = {}
            data['label'] = str(key.updated_at.date())
            data['value'] = int(key.current_price)
            dataSource['data'].append(data)
    
            # Create an object for the Column 2D chart using the FusionCharts class constructor
        column2D = FusionCharts("column2D", "ex1", "1300", "550", "chart-1", "json", dataSource)
        # return render(request, 'index.html', {'output': column2D.render()})
        
        print(id)
        print(column2D)
        return render(request, "graph.html", {'output': column2D.render(), "Login": "True"})
    
    return redirect("/")