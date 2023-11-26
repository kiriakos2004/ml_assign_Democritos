from django.shortcuts import render
from . import ml_model
from . import dict

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
            rpm = dict.dict_of_attributes['ME RPM'][0]
        try:
            aft_draft = float(request.POST.get('aft_draft'))
        except:
            aft_draft = dict.dict_of_attributes['AFT DRAFT'][0]
        try:            
            fore_draft = float(request.POST.get('fore_draft'))
        except:
            fore_draft = dict.dict_of_attributes['FORE DRAFT'][0]
        try:              
            heading = request.POST.get('heading')
        except:
            heading = dict.dict_of_attributes['HEADING'][0]         
        rpm = ml_model.test(rpm)
        return render(request, 'prediction.html', {'rpm':rpm})
    else:
        return render(request, 'prediction.html', {})
    
