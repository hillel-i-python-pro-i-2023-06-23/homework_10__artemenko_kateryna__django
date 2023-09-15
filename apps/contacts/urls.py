from django.urls import path

from . import views

app_name = "contacts"

urlpatterns = [
    path("list/", views.ContactsListView.as_view(), name="contacts_list"),
    path("create/", views.ContactsCreateView.as_view(), name="contacts_create"),
    path("update/<int:pk>/", views.ContactsUpdateView.as_view(), name="contacts_update"),
    path("delete/<int:pk>/", views.ContactsDeleteView.as_view(), name="contacts_delete"),
    path("generate/", views.generate_contacts_view, name="contacts_generate"),
    path("delete/", views.delete_contacts_view, name="contacts_delete"),
]
