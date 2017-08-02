from django.http import HttpResponse
from .models import Post # importando bd 
from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'polls/post_list.html', {})	