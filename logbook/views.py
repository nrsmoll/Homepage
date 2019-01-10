from django.shortcuts import render

from logbook.models import Consultation, Procedure


def index(request):
    return render(request, 'index.html')

def logbook_index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_cases = Consultation.objects.all().count()
    num_medical = Consultation.objects.filter(specialty=1).count()
    num_pediatric = Consultation.objects.filter(specialty=3).count()
    num_og = Consultation.objects.filter(specialty=11).count()
    num_trauma = Consultation.objects.filter(specialty=6).count()
    num_anesthetics = Consultation.objects.filter(specialty=14).count()
    num_pallcare = Consultation.objects.filter(specialty=5).count()

    # Total Procedures
    num_procedures = Procedure.objects.all().count()

    context = {
        'num_cases': num_cases,
        'num_medical': num_medical,
        'num_pediatric': num_pediatric,
        'num_og': num_og,
        'num_trauma': num_trauma,
        'num_anesthetics': num_anesthetics,
        'num_pallcare': num_pallcare,
        'num_procedures': num_procedures,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'logbook_index.html', context=context)

def publications(request):
    return render(request, 'publications.html')