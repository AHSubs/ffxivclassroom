from django.shortcuts import render

# Create your views here.

def job_list(request):
    return render(request,'ffxivjob/job_list.html',{})