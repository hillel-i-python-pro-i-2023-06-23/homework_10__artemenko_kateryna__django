from django.db import models

from .group import Group


class Contact(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.CharField(max_length=15, null=True, blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        blank=False,
        null=False,
    )

    colors = models.ManyToManyField(
        Group,
        related_name="animals",
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        ordering = ["-modified_at", "name"]
