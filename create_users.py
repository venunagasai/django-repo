import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_abacus.settings')
django.setup()

from django.contrib.auth.models import User

# Create main user
if not User.objects.filter(username='muralikrishna').exists():
    User.objects.create_user('muralikrishna', 'muralikrishna@example.com', 'hello sir')
    print("User muralikrishna created")
else:
    u = User.objects.get(username='muralikrishna')
    u.set_password('hello sir')
    u.save()
    print("User muralikrishna updated")

# Create generic user
users = [
    ('johndoe', 'password123'),
    ('venu', 'venu123'),
    ('vikram', 'vikram123'),
    ('venu naga sai','Venu@1234'),
    ('vivek', 'vivek123'),
]

for username, pwd in users:
    if not User.objects.filter(username=username).exists():
        User.objects.create_user(username, f'{username}@example.com', pwd, first_name=username.capitalize())
        print(f"User {username} created")
    else:
        u = User.objects.get(username=username)
        u.set_password(pwd)
        u.first_name = username.capitalize()
        u.save()
        print(f"User {username} updated")
