from django.urls import path

from . import views

app_name='reminder'
urlpatterns = [
    path('', views.index, name='index'),
    path('make', views.make, name='make')
]