from django.shortcuts import render
from .models import Base,Job
from django.utils import timezone
# Create your views here.

def classlist(request):
    baselist = Base.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request,'class_list/classlist.html',{'baselist':baselist})

def joblist(request):
    listjob = Job.objects.filter(pub_date__lte=timezone.now()).oder_by('pub_date')
    return render(request,'class_list/joblist.html',{'listjob':listjob})