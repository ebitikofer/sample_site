from django.http import HttpResponse
from django.template import loader
from .models import Link
from .models import File

def index(request):
    all_links = Link.objects.all() 
    html = ''
    for link in all_links:
        html += '<a href = "' + link.link + '">' + link.title + '</a><br>'
    return HttpResponse(html)

def detail(request, fid):
    file = File.objects.get(id=fid)
    template = loader.get_template('register/project.html')
    context = {
        'file': file,
    }
    #html = file.title + '<br>' + file.author + '<br>' + file.location + '<br>' + file.rating + '<br>' + file.type + '<br><br>' + file.description + '<br>'
    return HttpResponse(template.render(context, request))