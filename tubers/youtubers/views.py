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
    print(ytuber)
    data = {
        'ytuber' : ytuber
    }
    return render(request, 'youtubers/youtuber.html', data)

def search(request):
    pass
