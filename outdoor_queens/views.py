""" Error Handling """
from django.shortcuts import render

def custom_404(request, exception):
    """ Render 404 page """
    return render(request, "404.html", status=404)

def custom_500(request):
    """ Render 500 page """
    return render(request, "500.html", status=500)