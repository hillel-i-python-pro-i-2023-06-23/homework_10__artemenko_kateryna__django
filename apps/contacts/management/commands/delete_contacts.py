from django.core.management.base import BaseCommand

from apps.contacts.services.delete_contacts import delete_contacts


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--is-only-auto-generated",
            help="Delete only auto generated contacts",
            action="store_true",
        )

    def handle(self, *args, **options):
        is_only_auto_generated: bool = options["is_only_auto_generated"]

        delete_contacts(is_only_auto_generated=is_only_auto_generated)
