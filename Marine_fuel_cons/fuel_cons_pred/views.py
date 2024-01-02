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
        list = var_creation.create_data_for_pred(duration, rpm, aft_draft, fore_draft, heading)
        list_of_labels = var_creation.create_labels(duration)
        data= [26900, 28700, 27300, 29200]
        com_cons = sum(data)
        return render(request, 'prediction.html', {'rpm':rpm, 'duration':duration, 'list':list, 'labels':list_of_labels,
                                                   'labels':list_of_labels, 'data':data, 'com_cons':com_cons})
    else:
        return render(request, 'prediction.html', {})

    
