from django.contrib import admin

from apps.contacts import models
from apps.contacts.models import Contact


# admin.site.register(models.Contact)


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "birthday",
        "created_at",
        "modified_at",
    )


class ContactInline(admin.TabularInline):
    model = Contact.groups.through
    extra = 0


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        "value",
        "created_at",
        "modified_at",
    )
    inlines = [ContactInline]
