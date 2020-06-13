from django.shortcuts import render
from .models import Post
from django.views import generic
from rest_framework import viewsets
#from .serializers import PostSerializer

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

""" class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('author')
    serializer_class = PostSerializer
 """