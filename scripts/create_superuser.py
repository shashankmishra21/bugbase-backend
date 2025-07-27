import os
import django

# ✅ Correct project settings path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bugbase.settings')

django.setup()

from django.contrib.auth.models import User

# 🔐 Create superuser if it doesn't exist
username = 'superuserShashank'
password = 'superuserbugbase'
email = 'shashank@bugbase.com'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, password=password, email=email)
    print(f"✅ Superuser '{username}' created.")
else:
    print(f"ℹ️ Superuser '{username}' already exists.")
