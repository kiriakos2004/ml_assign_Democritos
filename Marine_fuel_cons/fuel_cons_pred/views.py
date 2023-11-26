from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def prediction(request):
    if request.method == 'POST':
        duration = request.POST.get('duration')
        speed = request.POST.get('speed')
        aft_draft = request.POST.get('aft_draft')
        fore_draft = request.POST.get('fore_draft')
        heading = request.POST.get('heading')     
    return render(request, 'prediction.html', {'speed':speed})
