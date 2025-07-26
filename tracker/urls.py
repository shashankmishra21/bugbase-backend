from django.urls import path
from .views import BugListCreateView, BugDetailView, CommentListCreateView
from rest_framework.authtoken.views import obtain_auth_token
from .auth_views import register_user
from .views import get_user_info
from .views import CommentListCreateView
from .views import export_bugs_csv
from .views import LoginView

urlpatterns = [
    path('bugs/', BugListCreateView.as_view(), name='bug-list-create'),
    path('bugs/<int:pk>/', BugDetailView.as_view(), name='bug-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
   path('login/', LoginView.as_view(), name='login'),
    path('register/', register_user, name='register'),
    path('user/', get_user_info, name='get-user-info'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('export-bugs/', export_bugs_csv, name='export-bugs'),
]
