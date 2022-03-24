#from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index),
    path('about-book', views.about),
    path('top-10', views.top),
    path('reminder', views.reminder),
]
