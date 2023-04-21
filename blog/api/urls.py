from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views

from blog.api.views import PostLists, PostDetail

urlpatterns = [
  path('posts/', PostLists.as_view(), name='api_post_list'),
  path('posts/<int:pk>', PostDetail.as_view(), name='api_post_detail'),
]

# rest framework authenticattion in case where is no any other form of it already tet up.
urlpatterns += [
  path('auth/', include('rest_framework.urls')),
  path("token-auth/", views.obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)