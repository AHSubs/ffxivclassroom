from django.shortcuts import render

# Create your views here.

def class_list(request):
    return render(request,'ffxivclass/class_list.html',{})