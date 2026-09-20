from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


def hello(request):
    return render(request, 'hello.html')


def resume(request, id) :
    user = get_object_or_404(User, id=id)
    context = {
        "user": user
    }
    return render(request, 'resume.html', context)