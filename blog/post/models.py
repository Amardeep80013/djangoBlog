from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=255)

  class Meta:
    ordering = ['name']
    verbose_name_plural = 'Categories'
  def __str__(self):
    return self.name

class Post(models.Model):
  category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  description = models.TextField()
  image = models.ImageField(upload_to='post_images', blank=True, null=True)
  created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title  