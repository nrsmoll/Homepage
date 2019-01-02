from django.shortcuts import render

from logbook.models import Consultation


def index(request):
    return render(request, 'index.html')

def logbook_index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_cases = Consultation.objects.all().count()

    # Total Procedures
    num_procedures = Consultation.objects.filter(case_type='2').count()

    context = {
        'num_cases': num_cases,
        'num_procedures': num_procedures,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'logbook_index.html', context=context)

def publications(request):
    return render(request, 'publications.html')