from django.shortcuts import render
from . import ml_model
from . import dict
from . import var_creation

def home(request):
    return render(request, 'home.html', {})

def prediction(request):
    if request.method == 'POST':
        try:
            duration = float(request.POST.get('duration'))
        except:
            duration=10
        try:
            rpm = float(request.POST.get('rpm'))
        except:
            rpm = 40
        try:
            aft_draft = float(request.POST.get('aft_draft'))
        except:
            aft_draft = dict.dict_of_attributes['AFT DRAFT'][0]
        try:            
            fore_draft = float(request.POST.get('fore_draft'))
        except:
            fore_draft = dict.dict_of_attributes['FORE DRAFT'][0]
        try:              
            heading = float(request.POST.get('heading'))
        except:
            heading = dict.dict_of_attributes['HEADING'][0]
        list_of_labels = var_creation.create_labels(duration)
        results = ml_model.results(var_creation.create_data_for_pred(duration, rpm, aft_draft, fore_draft, heading))
        com_cons = round(sum(results),2)
        return render(request, 'prediction.html', {'duration':duration, 'com_cons':com_cons, 'labels':list_of_labels, 'results':results})
    else:
        return render(request, 'prediction.html', {})
