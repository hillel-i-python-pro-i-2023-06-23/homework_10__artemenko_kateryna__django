from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from apps.contacts.models import Contact
from apps.contacts.services.delete_contacts import delete_contacts


class ContactsListView(ListView):
    model = Contact


class ContactsCreateView(CreateView):
    model = Contact
    fields = ("name", "phone")
    success_url = reverse_lazy("contacts:contacts_list")


class ContactsUpdateView(UpdateView):
    model = Contact
    fields = ("name", "phone")
    success_url = reverse_lazy("contacts:contacts_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


class ContactsDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy("contacts:contacts_list")


def generate_contacts_view(request):
    return render(
        request=request,
        template_name="contacts/contact_generate.html",
        context=dict(
            contacts_list=Contact.objects.all(),
        ),
    )


def delete_contacts_view(request):
    delete_contacts()

    return redirect(reverse_lazy("contacts:contacts_list"))
