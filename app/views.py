"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from rest_framework import generics
from .models import Cities
from .serializers import CitiesSerializer


#FORMS
from .forms import CitiesForm

#FOR DJANGO REST API
class CitiesList(generics.ListAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'add_city': CitiesForm(),
        }

    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


class FormActions:

    def __init__(self):
        pass

    def create_city(self, request):
        if request.method == 'POST':
            form = CitiesForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = CitiesForm()
        return home
