from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from .serializer import PostSerializer

# Create your views here.
class ApiPageView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer