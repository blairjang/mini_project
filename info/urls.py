from django.urls import path,include
from info import views
urlpatterns = [    
    path("", views.index),
]
