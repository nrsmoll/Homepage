from datetime import datetime, timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F, ExpressionWrapper, DurationField
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from logbook.forms import ConsultationForm
from logbook.models import Consultation
from logbook.models import Procedure


def index(request):
    return render(request, 'index.html')

def logbook_index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_cases = Consultation.objects.all().count()
    num_medical = Consultation.objects.filter(specialty=1).count()

    num_pediatric = Consultation.objects.annotate(age=ExpressionWrapper(F('date_of_contact') - F('date_of_birth'),
                    output_field=DurationField())).filter(age__lte=timedelta(days=6574.32)).count()

    num_og = Consultation.objects.filter(specialty=11).count()
    num_trauma = Consultation.objects.filter(specialty=6).count()
    num_burns = Consultation.objects.filter(specialty=7).count()
    num_pallcare = Consultation.objects.filter(specialty=5).count()

    num_diagnostic = Procedure.objects.filter(procedure_class=1).count()
    num_vascularaccess = Procedure.objects.filter(procedure_class=3).count()
    num_therapeutic = Procedure.objects.filter(procedure_class=2).count()
    num_anesthesia = Procedure.objects.filter(procedure_class=4).count()

    # Total Procedures
    num_procedures = Procedure.objects.all().count()

    context = {
        'num_cases': num_cases,
        'num_medical': num_medical,
        'num_pediatric': num_pediatric,
        'num_og': num_og,
        'num_trauma': num_trauma,
        'num_burns': num_burns,
        'num_pallcare': num_pallcare,
        'num_procedures': num_procedures,
        'num_diagnostic': num_diagnostic,
        'num_vascularaccess': num_vascularaccess,
        'num_therapeutic': num_therapeutic,
        'num_anesthesia': num_anesthesia,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'logbook_index.html', context=context)

def publications(request):
    return render(request, 'publications.html')


class ConsultationCreate(LoginRequiredMixin, CreateView):
    model = Consultation
    form_class = ConsultationForm
    success_url = reverse_lazy('logbook_index')


class ConsultationUpdate(LoginRequiredMixin, UpdateView):
    model = Consultation
    form_class = ConsultationForm
    template_name = 'logbook/consultation_update_form.html'
    success_url = reverse_lazy('consultation_list')


class ConsultationDelete(LoginRequiredMixin, DeleteView):
    model = Consultation
    success_url = reverse_lazy('logbook_index')


class ConsultationList(LoginRequiredMixin, ListView):
    model = Consultation
    paginate_by = 10
    context_object_name = 'my_recent_consultation_list'  # your own name for the list as a template variable
    last_month = datetime.today() - timedelta(days=30)
    queryset = Consultation.objects.filter(date_of_contact__gte=last_month).order_by('-date_of_contact')
    # template_name = 'logbook/consultation_list.html'  # Specify your own template name/location
