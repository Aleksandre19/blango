from rest_framework import generics

from blog.api.serializers import PostSerializer, UserSerializer
from blog.models import Post

from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject

class PostLists(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_calsses = [AuthorModifyOrReadOnly | IsAdminUserForObject]
  queryset = Post.objects.all()
  serializer_class = PostSerializer

class UserDetail(generics.RetrieveAPIView):
  lookup_field = 'email'
  queryset = User.objects.all()
  serializer_class = UserSerializer