from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns



class Consultation(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    uid = models.CharField(max_length=20, verbose_name='UID')
    name = models.CharField(max_length=400)
    date_of_birth = models.DateField(blank=True, null=True)
    GENDER_CHOICES = (
        (str(1), 'Male'),
        (str(2), 'Female'))
    sex = models.CharField(choices=GENDER_CHOICES, max_length=30)
    date_of_contact = models.DateField(null=False)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    post_code = models.CharField(max_length=12, verbose_name='Post Code')
    specialty = models.ForeignKey('Specialty', on_delete=models.SET_NULL, null=True)
    diagnosis = models.CharField(max_length=400, verbose_name='Working Diagnosis')
    supervision_list = (
        (str(1), 'Senior Practitioner'),
        (str(2), 'Supervised'),
        (str(3), 'Observed'),)
    supervision = models.CharField(
        max_length=128,
        choices=supervision_list,
        default=1, )
    notes = models.TextField(max_length=1000, help_text='Enter a description of the consultation')

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('case-detail', kwargs={'pk': self.pk})

    def __str__(self):
        """String for representing the Model object."""
        return self.name + ' - ' + str(self.date_of_contact) + ' - ' + str(self.specialty)


class Procedure(models.Model):
    """Model representing a procedure type."""
    uid = models.CharField(max_length=20, verbose_name='UID')
    name = models.CharField(max_length=400)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    date_of_birth = models.DateField(verbose_name='Date of Birth')
    date_of_contact = models.DateField(null=False, verbose_name='Procedure Date')
    GENDER_CHOICES = (
        (str(1), 'Male'),
        (str(2), 'Female'))
    sex = models.CharField(choices=GENDER_CHOICES, max_length=30, verbose_name='Gender')
    procedure_name = models.CharField(max_length=128, null=False)
    procedure_class = models.ForeignKey('Procedure_Class', on_delete=models.SET_NULL, null=True)
    procedure_list = (
        (str(2), 'Diagnostic'),
        (str(1), 'Therapeutic'),)
    procedure_type = models.CharField(
        max_length=256,
        choices=procedure_list,
        default=1, )
    specialty = models.ForeignKey('Specialty', on_delete=models.SET_NULL, null=True)
    diagnosis = models.CharField(max_length=400, verbose_name='Working Diagnosis')

    supervision_list = (
        (str(1), 'Senior Practitioner'),
        (str(2), 'Supervised'),
        (str(3), 'Observed'),)
    supervision = models.CharField(
        max_length=128,
        choices=supervision_list,
        default=1, )
    notes = models.TextField(max_length=1000, help_text='Enter a description of the case')

    def __str__(self):
        """String for representing the Model object."""
        return self.name + ' - ' + self.procedure_name + ' - ' + str(self.date_of_contact)


class Specialty(models.Model):
    class Meta:
        verbose_name_plural = "Specialties"

    """Model representing a specialty type."""
    specialty = models.CharField(max_length=128)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.specialty}'


class Procedure_Class(models.Model):
    class Meta:
        verbose_name_plural = "Procedure Classes"

    """Model representing a specialty type."""
    procedure_class = models.CharField(max_length=128)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.procedure_class}'


class Location(models.Model):
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
