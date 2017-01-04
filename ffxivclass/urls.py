from django.conf.urls import url
from . import views

urlpatterns=[
   url(r'^$',views.class_list,name='class_list')
]
