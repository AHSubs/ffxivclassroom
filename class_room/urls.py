from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^classi',views.classlist,name='class_list'),
    url(r'^jobs',views.joblist,name='job_list'),
    url(r'^classe/(?P<pk>\d+)/$', views.classdetail, name='class_detail'),
    url(r'^job/(?P<pk>\d+)/$', views.jobdetail, name='job_detail'),
]