from django.db import models

from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


class Case(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    name = models.CharField(max_length=400)
    date_of_contact = models.DateField(null=False)
    case_types_list = (
        (str(1), 'Consultation'),
        (str(2), 'Procedure'),)
    case_type = models.CharField(
        max_length=256,
        choices=case_types_list,
        default=1, )
    case_specialty_list = (
        (str(1), 'General Practice'),
        (str(2), 'Internal Medicine'),
        (str(3), 'Surgery'),
        (str(4), 'Pain Medicine'),
        (str(5), 'Anesthetics'),
        (str(6), 'Paediatrics'),
        (str(7), 'Mental Health'),
        (str(8), 'Opthalmology'),
        (str(9), 'Orthopedics'),
        (str(10), 'Trauma'),
        (str(11), 'Obstetrics & Gynaecology'),
    )
    case_specialty = models.CharField(
        max_length=256,
        choices=case_specialty_list,
        default=1, )
    duration = models.CharField(max_length=5, help_text='minutes')
    location = models.ForeignKey('Locations', on_delete=models.SET_NULL, null=True)
    procedure = models.ForeignKey('Procedures', on_delete=models.SET_NULL, null=True)
    notes = models.TextField(max_length=1000, help_text='Enter a description of the case')

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('case-detail', kwargs={'pk': self.pk})

    def __str__(self):
        """String for representing the Model object."""
        return self.name + ' - ' + str(self.date_of_contact) + ' - ' + str(
            self.case_type) + ' - ' + str(self.case_specialty)


class Procedures(models.Model):
    """Model representing a procedure type."""
    procedure = models.CharField(max_length=100)
    procedure_list = (
        (str(2), 'Diagnostic'),
        (str(1), 'Therapeutic'),)
    procedure_type = models.CharField(
        max_length=256,
        choices=procedure_list,
        default=1, )

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.procedure}'


class Locations(models.Model):
    """Model representing a procedure type."""
    location = models.CharField(max_length=200)
    location_list = (
        (str(1), 'Hospital'),
        (str(2), 'Community'),)
    location_type = models.CharField(
        max_length=256,
        choices=location_list,
        default=1, )

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.location}'
