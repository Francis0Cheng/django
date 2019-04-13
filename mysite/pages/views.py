from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello</h1>")
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})


def about_view(request, *args, **kwargs):
    context = {
        'Hello': "你好",
        "lala": "啦啦啦",
        'my_list': [1, 2, 3, 5],
        'my_html': '<h1>Hello World</h1>'
    }
    return render(request, 'about.html', context)
