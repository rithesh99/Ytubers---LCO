from django.shortcuts import render
from .models import Slider, Team
from youtubers.models import Youtuber

# Create your views here.
def home(request):
    sliders = Slider.objects.all()
    team = Team.objects.all()
    featured_ytubers = Youtuber.objects.order_by('-created_at').filter(is_featured=True)
    ytubers = Youtuber.objects.order_by('-created_at')
    data = {
        'sliders' : sliders,
        'teams' : team,
        'featured_ytubers' : featured_ytubers,
        'ytubers' : ytubers
    }
    return render(request, 'webpages/home.html', data)

def about(request):
    return render(request, 'webpages/about.html')

def services(request):
    return render(request, 'webpages/services.html')

def contact(request):
    return render(request, 'webpages/contact.html')   