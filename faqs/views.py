from django.shortcuts import render
from .models import FAQ
from .forms import ContactForm

# Create your views here.
def faqs_view(request):
    faqs = FAQ.objects.all().order_by('order')
    contact_form = ContactForm()

    return render(request, 'faqs/faqs.html', {'faqs': faqs, 'contact_form': contact_form},)