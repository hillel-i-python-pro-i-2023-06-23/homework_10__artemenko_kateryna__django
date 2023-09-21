from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        queryset = get_user_model().objects.all()

        base_name = "admin"
        base_email = "admin@gmail.com"
        base_password = "admin123"
        if not queryset.filter(username=base_name).exists():
            get_user_model().objects.create_superuser(
                username=base_name,
                email=base_email,
                password=base_password,
            )
