from rest_framework import generics
from .models import Bug, Comment
from .serializers import BugSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from .ai_utils import generate_ai_suggestion
from rest_framework.authentication import TokenAuthentication
from .permissions import IsOwnerOrSuperUser  
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import HttpResponse
import csv

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
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        bug_id = self.request.query_params.get('bug')
        return Comment.objects.filter(bug_id=bug_id) if bug_id else Comment.objects.all()

    def perform_create(self, serializer):
        # This allows any authenticated user to add comment
        serializer.save(created_by=self.request.user)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    return Response({
        'id': request.user.id,  
        'username': request.user.username,
        'is_superuser': request.user.is_superuser,
    })

@api_view(['GET'])
@permission_classes([IsAdminUser])
def export_bugs_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="bugs.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Title', 'Description', 'Status', 'AI Suggestion', 'Created At', 'Created By'])

    for bug in Bug.objects.all():
        writer.writerow([
            bug.id,
            bug.title,
            bug.description,
            bug.status,
            bug.ai_suggestion,
            bug.created_at,
            bug.created_by.username  # Or bug.created_by_id if no related user object
        ])

    return response