from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('topics/topic_id',views.topic),
    path('result/',views.results, name = "results"),
]