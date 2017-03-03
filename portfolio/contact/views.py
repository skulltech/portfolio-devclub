from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.send()

    return render(request, 'contact/contact.html', {'form': form})