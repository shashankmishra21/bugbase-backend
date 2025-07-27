from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
import json

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password required'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        token = Token.objects.create(user=user)

        return Response({'token': token.key, 'user_id': user.id, 'username': user.username}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    try:
        data = json.loads(request.body)
        print("🔥 Incoming Login Request")
        print("🔥 Headers:", dict(request.headers))
        print("🔥 Raw body:", request.body)
        print("🔥 Parsed data:", data)

        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password required'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.id,
                'username': user.username,
                'is_superuser': user.is_superuser
            })
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    except json.JSONDecodeError:
        return Response({'error': 'Invalid JSON'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
