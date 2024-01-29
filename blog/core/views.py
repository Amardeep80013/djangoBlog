from django.shortcuts import render, redirect
from post.models import Category, Post
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def index(request):
  post = Post.objects.all().order_by('-created_at')[0:6]
  category = Category.objects.all()
  context = {
    'posts': post,
    'categories': category,
  }
  return render(request, 'core/index.html', context)

def signup(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)

    if form.is_valid():
      form.save()

      return redirect('/login/')
  
  else:
    form = SignupForm()
  
  context = {
    'form': form,
  }
  return render(request, 'core/signup.html', context)

def loginUser(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')
    print(email,' , ', password)
    username = User.objects.filter(email=email).first()
    user = authenticate(request, username=username, password=password)

    if user is None:
      messages.success(request, 'Wrong email and password...')
      return redirect('/login/')
    
    else:
      login(request, user)
      return redirect('/')
    
  else:
    form = LoginForm()
  
  context = {
    'form': form,
  }

  return render(request, 'core/login.html', context)

def logoutUser(request):
  logout(request)
  return redirect('/')