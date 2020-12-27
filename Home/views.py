from django.shortcuts import render
from Home.models import Work
from datetime import datetime
from django.contrib.messages import constants as messages
from django.contrib import messages


# Create your views here.


def index(request):
    contex = {'name': 'Shohag'}

    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']

        works = Work(title=title, desc=desc, date=datetime.today())
        works.save()
        messages.success(request, 'Your tasks is submittes!!')

    return render(request, 'index.html', contex)


def tasks(request):

    alltasks = Work.objects.all()
    context = {'tasks': alltasks}
    return render(request, 'tasks.html', context)
