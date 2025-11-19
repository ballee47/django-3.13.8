"""
URL configuration for mainapp1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from .import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', views.home1,name="home"),
    path('logged/', views.loggedin,name="loggedin"),
    path('join/', views.join12345,name="joinpage"),
    path('page2/', views.page2, name='page2'),  # category list
    path('page2/<str:category>/', views.page2_category, name='page2_category'),  # games in category
    path('page2/<str:category>/<int:id>/<str:names>/', views.page2_detail, name='page2_detail'),  # game details
    path('join2/', views.join1234,name="joinpage2"),
    path('login/', views.login1,name="loginpage"),
    path('logout/', views.logout1,name="logoutpage"),
    path('app1/', include('ch_1.urls'),),
    path('success/',views.data2,name='success'),
    path('success/<successForm>',views.data2a,),
    path('confirmation/',views.data3,name='confirmation1'),
    path('profile/',views.view_profile,name='profile1'),
    path('list_gamers/',views.list_gamer,name='list_gamers'),
    path('update/<int:id>/', views.update_gamer, name='update_gamer'),
    path('delete/<int:id>/', views.delete_gamer, name='delete_gamer'),


 

         

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
