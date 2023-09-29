from django.contrib import admin

from apps.contacts import models


# admin.site.register(Contact)


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created_at",
        "modified_at",
    )


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        "value",
        "created_at",
        "modified_at",
    )
