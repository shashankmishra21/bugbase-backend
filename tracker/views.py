from rest_framework import generics
from .models import Bug, Comment
from .serializers import BugSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from .ai_utils import generate_ai_suggestion
from rest_framework.authentication import TokenAuthentication
from .permissions import IsOwnerOrSuperUser  
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# List all bugs or create a new one
class BugListCreateView(generics.ListCreateAPIView):
    queryset = Bug.objects.all()
    serializer_class = BugSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        title = self.request.data.get('title', '')
        description = self.request.data.get('description', '')
        suggestion = generate_ai_suggestion(title, description)

        serializer.save(
            created_by=self.request.user,
            ai_suggestion=suggestion
        )

#  Get, update, or delete a specific bug
class BugDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bug.objects.all()
    serializer_class = BugSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrSuperUser]

#  List all comments or add a new one
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    return Response({
        'id': request.user.id,  
        'username': request.user.username,
        'is_superuser': request.user.is_superuser,
    })
