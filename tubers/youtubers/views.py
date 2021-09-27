from django.shortcuts import render, get_object_or_404
from .models import Youtuber

# Create your views here.
def youtubers(request):
    ytubers = Youtuber.objects.order_by('-created_at')
    data = {
        'ytubers' : ytubers
    }
    return render(request, 'youtubers/youtubers.html', data)

def youtubers_detail(request, id):
    ytuber = get_object_or_404(Youtuber, pk=id)
    data = {
        'ytuber' : ytuber
    }
    return render(request, 'youtubers/youtuber.html', data)

def search(request):
    ytubers = Youtuber.objects.order_by('-created_at')
    city_options = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_options = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_options = Youtuber.objects.values_list('category', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            ytubers = ytubers.filter(description__icontains=keyword)
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            ytubers = ytubers.filter(city__icontains=city)
    
    if 'camera' in request.GET:
        camera = request.GET['camera']
        if camera:
            ytubers = ytubers.filter(camera_type__icontains=camera)
    
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            ytubers = ytubers.filter(category__icontains=category)
    
    data = {
        'ytubers' : ytubers,
        'city_options' : city_options,
        'camera_options' : camera_options,
        'category_options' : category_options
    }
    return render(request, 'youtubers/search.html', data)
