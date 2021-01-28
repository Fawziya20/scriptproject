from django.shortcuts import render

# Create your views here.

def cylindervolume(request):
    context = {}
    return render(request, 'mathapp/cylindervolume.html', context)

def trianglearea(request):
    context = {}
    return render(request, 'mathapp/trianglearea.html', context)