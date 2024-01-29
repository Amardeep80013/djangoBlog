from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
  path('', views.browsePost, name='browse'),
  path('<int:pk>', views.detail, name='detail'),
  path('newpost/', views.newPost, name='newpost'),
  path('delete/<int:pk>', views.delete, name='delete'),
  path('edit/<int:pk>', views.edit, name='edit'),
  path('edit/<int:pk>', views.edit, name='edit'),
]