from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
	return HttpResponse(Post.objects.all())
	