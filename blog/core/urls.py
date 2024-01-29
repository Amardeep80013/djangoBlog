from django.urls import path
from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
  path('', views.index, name='index'),
  path('signup/', views.signup, name='signup'),
  path('login/', views.loginUser, name='login'),
  path('logout/', views.logoutUser, name='logout'),
]