from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
app_name='myapp'

urlpatterns = [
    path('',views.input_form,name='input'),
    path('content/',views.display,name='display'),
    path('content/<int:pk>',views.delete,name='delete'),
   # path('appoint/video',views.video,name='video')$
]
