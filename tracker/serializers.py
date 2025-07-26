from rest_framework import serializers
from .models import Bug, Comment

class BugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = '__all__'
        read_only_fields = ['created_by', 'ai_suggestion', 'created_at']
        
class CommentSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'bug', 'text', 'created_by', 'created_at']
