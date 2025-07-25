from django.urls import path
from .views import BugListCreateView, BugDetailView, CommentListCreateView
from rest_framework.authtoken.views import obtain_auth_token
from .auth_views import register_user

urlpatterns = [
    path('bugs/', BugListCreateView.as_view(), name='bug-list-create'),
    path('bugs/<int:pk>/', BugDetailView.as_view(), name='bug-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('register/', register_user, name='register'),
]
