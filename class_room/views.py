from django.shortcuts import render,get_object_or_404
from .models import Base,Job
from django.utils import timezone
# Create your views here.

def classlist(request):
    baselist = Base.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request,'classlist.html',{'baselist':baselist})

def joblist(request):
    listjob = Job.objects.filter(pub_date__lte=timezone.now()).oder_by('pub_date')
    return render(request,'joblist.html',{'listjob':listjob})

def classdetail(request,pk):
    classe = get_object_or_404(Base,pk=pk)
    return render(request,'classdetail.html',{'classe':classe})

def jobdetail(request,pk):
    job = get_object_or_404(Job,pk=pk)
    return render(request,'jobdetail.html',{'job':job})
