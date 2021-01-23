from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('addcity',views.addcity,name='addcity'),  
    path('delete/<city_name>/',views.delete,name='delete'),  
]
