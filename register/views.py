from django.http import HttpResponse
from .models import Link

def index(request):
    all_links = Link.objects.all() 
    html = ''
    for link in all_links:
        html += '<a href = "' + link.link + '">' + link.title + '</a><br>'
    return HttpResponse(html)