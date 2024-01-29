from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from post.models import Post

# Create your views here.
@login_required
def dashboard(request):
  post = Post.objects.filter(created_by=request.user)
  context = {
    'posts': post,
  }
  return render(request, 'dashboard/dashboard.html', context)