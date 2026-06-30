from django.contrib.auth.models import User

username = "figleaf"
email = "figleaf@gmail.com"
password = "figleaf123"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("Admin user created.")
else:
    print("Admin user already exists.")