from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post



def first_program(request):
    # template = loader.get_template("index.html")
    context = {
        'content':Post.objects.all()
    }
    return render(request,'home.html',context)


    # return HttpResponse(template.render())

# Create your views here.
def about(request):
    # data = {"contxt": "i am the best..."}
   # return render(request, 'about.html',data)

    return render(request, 'about.html',{'title':'about'})