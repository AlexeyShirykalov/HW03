from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index1(request):
    return render(request, 'page1/index.html', {'content': 'Your content here.'})

def index2(request):
    return render(request, 'page2/index.html', {'content': 'Your content here.'})

@login_required()
def index3(request):
    return render(request, 'page3/index.html', {'content': 'Your content here.'})