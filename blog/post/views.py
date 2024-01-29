from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category
from django.contrib.auth.decorators import login_required
from .forms import newPostForm, editPostForm
from django.db.models import Q
# Create your views here.
def browsePost(request):
  query = request.GET.get('query', '')
  category_id = request.GET.get('category', 0)
  categories = Category.objects.all()
  post = Post.objects.all()

  if query:
    post = post.filter(Q(title__icontains=query) | Q(description__icontains=query))

  if category_id:
    post = post.filter(category=category_id)

  context = {
    'posts': post,
    'query': query,
    'categories': categories,
    'category_id': int(category_id),
  }
  return render(request, "post/browsepost.html", context)

def detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  related_post = Post.objects.filter(category=post.category).exclude(pk=pk)[0:3]
  context = {
    'post': post,
    'related_posts': related_post,
  }

  return render(request, 'post/detail.html', context)

@login_required
def newPost(request):
  if request.method == 'POST':
    form = newPostForm(request.POST, request.FILES)

    if form.is_valid():
      post = form.save(commit=False)
      post.created_by = request.user
      post.save()

      return redirect('post:detail', pk=post.pk)
  
  else:
    form = newPostForm()
  context = {
    'type': 'Add',
    'form': form,
    'title': 'Add Post',
    'btn': 'Add'
  }
  return render(request,'post/newpost.html', context)

@login_required
def edit(request, pk):
  post = get_object_or_404(Post, pk=pk, created_by=request.user)
  # print(post)
  if request.method == 'POST':
    # print('hello')
    form = editPostForm(request.POST, request.FILES, instance=post)
    # print(form)
    if form.is_valid():
      form.save()

      return redirect('post:detail', pk=post.pk)
  else:
    form = editPostForm(instance=post)
  context = {
    'pk': pk,
    'type': 'Edit',
    'form': form,
    'title': 'Edit Post',
    'btn': 'Edit'
  }
  return render(request, 'post/newpost.html', context)

@login_required
def delete(request, pk):
  post = get_object_or_404(Post, pk=pk, created_by=request.user)
  post.delete()
  return redirect('dashboard:dashboard')

 