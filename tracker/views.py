from rest_framework import generics
from .models import Bug, Comment
from .serializers import BugSerializer, CommentSerializer

# 🐞 List all bugs or create a new one
class BugListCreateView(generics.ListCreateAPIView):
    queryset = Bug.objects.all()
    serializer_class = BugSerializer

# 🔍 Get, update, or delete a specific bug
class BugDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bug.objects.all()
    serializer_class = BugSerializer

# 💬 List all comments or add a new one
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
