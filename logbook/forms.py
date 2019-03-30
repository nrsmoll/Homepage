from bootstrap_datepicker_plus import DatePickerInput
from django import forms

from logbook.models import Consultation


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['uid', 'name', 'date_of_birth', 'sex', 'date_of_contact', 'location', 'post_code', 'specialty',
                  'diagnosis', 'supervision', 'sentiment', 'notes']
        widgets = {
            'date_of_birth': DatePickerInput(),  # default date-format %m/%d/%Y will be used
            'date_of_contact': DatePickerInput(),  # default date-format %m/%d/%Y will be used
        }
