from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('hello/<str:name>', views.hello),
    path('times2/<int:number>', views.times2),
    path('total/<int:number>', views.total),
    path('addCup/', views.addCup),
    path('createCup/', views.createCup),
]