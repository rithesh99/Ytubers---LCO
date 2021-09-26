from django.shortcuts import render
from .models import Slider, Team

# Create your views here.
def home(request):
    sliders = Slider.objects.all()
    team = Team.objects.all()
    data = {
        'sliders' : sliders,
        'teams' : team
    }
    return render(request, 'webpages/home.html', data)

def about(request):
    return render(request, 'webpages/about.html')

def services(request):
    return render(request, 'webpages/services.html')

def contact(request):
    return render(request, 'webpages/contact.html')   