from . import views
from django.urls import path, include
from rest_framework import routers

""" router = routers.DefaultRouter()
router.register(r'title', views.PostViewSet) """

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    #path('posts/', include(router.urls)),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]