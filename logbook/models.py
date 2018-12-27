from django.db import models

from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


class Case(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
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
        (str(4), 'Obstetrics & Gynaecology'),
        (str(5), 'Anesthetics'),
        (str(6), 'Paediatrics'),
        (str(7), 'Mental Health'),
        (str(8), 'Opthalmology'),
        (str(9), 'Orthopedics'),
        (str(10), 'Trauma'),)
    case_specialty = models.CharField(
        max_length=256,
        choices=case_specialty_list,
        default=1, )

    procedure = models.ForeignKey('Procedures', on_delete=models.SET_NULL, null=True)
    notes = models.TextField(max_length=1000, help_text='Enter a description of the case')

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('case-detail', kwargs={'pk': self.pk})

    def __str__(self):
        """String for representing the Model object."""
        return self.firstname + ' ' + self.lastname + ' - ' + str(self.date_of_contact)


class Procedures(models.Model):
    """Model representing an author."""
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