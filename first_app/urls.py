from django.urls import path
from .import views
urlpatterns = [
    path('', views.home ,name='home'),
    path('signUp/', views.signUP ,name='signUp'),
    path('login/', views.Login ,name='login'),
    path('profile/', views.profile ,name='profile'),
    path('logout/', views.LogOut ,name='logout'),
    path('pass_change/', views.pass_change ,name='pass_change'),
    path('pass_change2/', views.pass_change2 ,name='pass_change2'),
]
