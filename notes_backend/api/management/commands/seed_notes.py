from django.core.management.base import BaseCommand
from api.models import Note


class Command(BaseCommand):
    help = "Create a few demo notes for testing"

    # PUBLIC_INTERFACE
    def handle(self, *args, **options):
        """Create a few sample notes if none exist."""
        if Note.objects.exists():
            self.stdout.write(self.style.WARNING("Notes already exist, skipping seeding."))
            return

        samples = [
            {"title": "Welcome to Simple Notes", "content": "This is your first note. Feel free to edit or delete it."},
            {"title": "Django REST API", "content": "CRUD endpoints available at /api/notes/"},
        ]
        for data in samples:
            Note.objects.create(**data)
        self.stdout.write(self.style.SUCCESS("Created demo notes."))
