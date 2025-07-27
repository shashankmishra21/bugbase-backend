from django.urls import path
from .views import BugListCreateView, BugDetailView, CommentListCreateView, get_user_info, export_bugs_csv
from .auth_views import register_user, login_user

urlpatterns = [
    path('bugs/', BugListCreateView.as_view(), name='bug-list-create'),
    path('bugs/<int:pk>/', BugDetailView.as_view(), name='bug-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('register/', auth_views.register_user),
    path('login/', auth_views.login_user),
    path('user/', get_user_info, name='get-user-info'),
    path('export-bugs/', export_bugs_csv, name='export-bugs'),
]
