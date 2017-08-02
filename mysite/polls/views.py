from .models import Post # importando bd 
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User

# Create your views here.
def index(request):
	autor = User.objects.get(username="admin")
	posts = Post.objects.filter(autor=autor)
	return render(request, 'polls/post_list.html', {'autor': autor,
													'posts': posts})	