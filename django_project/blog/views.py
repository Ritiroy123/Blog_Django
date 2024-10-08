from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


posts = [
    {
        'author':'ritika',
        'title': 'Blog_post_1',
        'content': 'first post content',
        'date_posted': '28 sept 2024'
    },
    {
        'author':'prince',
        'title': 'Blog_post_2',
        'content': 'second post content',
        'date_posted': '30 sept 2024'
    }
]
def first_program(request):
    # template = loader.get_template("index.html")
    context = {
        'content':posts
    }
    return render(request,'home.html',context)


    # return HttpResponse(template.render())

# Create your views here.
def about(request):
    # data = {"contxt": "i am the best..."}
   # return render(request, 'about.html',data)

    return render(request, 'about.html',{'title':'about'})