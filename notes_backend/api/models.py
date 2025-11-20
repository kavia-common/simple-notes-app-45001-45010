from django.db import models


class Note(models.Model):
    """
    Model representing a note with a title and content.
    """
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)  # set once at creation
    updated_at = models.DateTimeField(auto_now=True)      # update on each save

    def __str__(self) -> str:
        return f"{self.id} - {self.title[:50]}"
