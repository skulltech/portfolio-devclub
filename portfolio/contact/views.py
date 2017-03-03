from django.shortcuts import render
from django.utils import timezone
from .forms import ContactForm
from .models import ContactMessage


def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        message = form.save(commit=False)
        message.send()

    return render(request, 'contact/contact.html', {'form': form})

def messages_list(request):
    messages = ContactMessage.objects.filter(submitted_date__lte=timezone.now()).order_by('submitted_date')
    return render(request, 'contact/messages_list.html', {'messages': messages})