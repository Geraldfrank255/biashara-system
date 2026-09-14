from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates an administrative user automatically'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = 'admin'
        email = 'admin@biashara.com'
        password = 'AdminPassword123!'

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
                role='admin'
            )
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully!'))
        else:
            self.stdout.write(self.style.WARNING(f'Superuser "{username}" already exists.'))
