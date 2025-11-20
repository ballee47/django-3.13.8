from django.urls import path
from . import views

urlpatterns = [
      path('', views.app1_fnc,name='app1p1'),
    # path('page1/', views.app1_fnc2),
    
]
