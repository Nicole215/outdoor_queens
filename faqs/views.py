from django.shortcuts import render
from .models import FAQ

# Create your views here.
def faqs_view(request):
    faqs = FAQ.objects.all().order_by('order')
    return render(request, 'faqs/faqs.html', {'faqs': faqs},)