from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import UserRegisterForm

from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)
@login_required
def about(request):
    return render(request, 'blog/about.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! you can now log in')
            return redirect('login')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})
    





