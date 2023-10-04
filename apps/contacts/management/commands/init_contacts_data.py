from django.core.management.base import BaseCommand

from apps.contacts import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        for group_as_str in ("Family", "Work", "Friend", "Travel"):
            models.Group.objects.get_or_create(value=group_as_str)
