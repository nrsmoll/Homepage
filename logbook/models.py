from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
from tinymce import models as tinymce_models


class Consultation(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    uid = models.CharField(max_length=20, verbose_name='UID', blank=True, null=True)
    name = models.CharField(max_length=400, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    GENDER_CHOICES = (
        (str(1), 'Male'),
        (str(2), 'Female'))
    sex = models.CharField(choices=GENDER_CHOICES, max_length=30, blank=True, null=True)
    date_of_contact = models.DateField(null=False)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True, blank=True)
    post_code = models.CharField(max_length=12, verbose_name='Post Code', blank=True, null=True)
    specialty = models.ForeignKey('Specialty', on_delete=models.SET_NULL, null=True, blank=True)
    diagnosis = models.CharField(max_length=400, verbose_name='Working Diagnosis', null=True, blank=True)
    supervision_list = (
        (str(1), 'Senior Practitioner'),
        (str(2), 'Supervised'),
        (str(3), 'Observed'),)
    supervision = models.CharField(
        max_length=128,
        choices=supervision_list,
        default=1, null=True)
    notes = models.TextField(max_length=20000,
                             help_text='Enter a description of the consultation.', blank=True, null=True)
    date_of_entry = models.DateTimeField(null=False, auto_now_add=True)

    direction_list = (
        (str(1), 'Worse'),
        (str(2), 'Unsure'),
        (str(3), 'No change'),
        (str(4), 'Better'),)
    sentiment = models.CharField(
        max_length=128,
        choices=direction_list,
        default=3, null=True, blank=True)

    @property
    def age(self):
        return int((self.date_of_contact - self.birth_date).days / 365.25)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this consultation."""
        return reverse('case-detail', kwargs={'pk': self.pk})

    def __str__(self):
        """String for representing the Model object."""
        return self.name + ' - ' + str(self.date_of_contact) + ' - ' + str(self.specialty)


class Procedure(models.Model):
    """Model representing a procedure type."""
    uid = models.CharField(max_length=20, verbose_name='UID', blank=True, null=True)
    name = models.CharField(max_length=400, null=True)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True, blank=True)
    date_of_birth = models.DateField(verbose_name='Date of Birth', blank=True, null=True)
    date_of_contact = models.DateField(verbose_name='Procedure Date', null=True, blank=True)
    GENDER_CHOICES = (
        (str(1), 'Male'),
        (str(2), 'Female'))
    sex = models.CharField(choices=GENDER_CHOICES, max_length=30, verbose_name='Gender', blank=True, null=True)
    procedure_name = models.CharField(max_length=128, null=True)
    procedure_class = models.ForeignKey('Procedure_Class', on_delete=models.SET_NULL, null=True)
    specialty = models.ForeignKey('Specialty', on_delete=models.SET_NULL, null=True)
    diagnosis = models.CharField(max_length=400, verbose_name='Working Diagnosis', null=True)

    supervision_list = (
        (str(1), 'Senior Practitioner'),
        (str(2), 'Supervised'),
        (str(3), 'Assisted'),
        (str(4), 'Observed'),)
    supervision = models.CharField(
        max_length=128,
        choices=supervision_list,
        default=1, )
    notes = tinymce_models.HTMLField(max_length=20000, help_text='Enter a description of the procedure', blank=True, null=True)
    date_of_entry = models.DateTimeField(null=False, auto_now_add=True)

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
        return str(self.pk) + ' - ' + self.specialty


class Procedure_Class(models.Model):
    class Meta:
        verbose_name_plural = "Procedure Classes"

    """Model representing a specialty type."""
    procedure_class = models.CharField(max_length=128)

    def __str__(self):
        """String for representing the Model object."""
        return str(self.pk) + ' - ' + self.procedure_class


class Location(models.Model):
    """Model representing a procedure type."""
    location = models.CharField(max_length=200)
    location_list = (
        (str(1), 'Hospital'),
        (str(2), 'General Practice'),
        (str(3), 'Emergency Department'),)
    location_type = models.CharField(
        max_length=256,
        choices=location_list,
        default=1, )

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.location}'
