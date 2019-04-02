from django import forms


class CpetForm(forms.Form):
    firstname = forms.CharField(label='First name', max_length=100)
    lastname = forms.CharField(label='Last name', max_length=100)
    age = forms.IntegerField(label='Age', max_value=110, min_value=0)
    bmi = forms.IntegerField(label='BMI', max_value=110, min_value=10)
    chronotropic = forms.IntegerField(label='Chronotropic Response', max_value=200, min_value=0)
    etco2 = forms.IntegerField(label='End-Tidal CO2', max_value=200, min_value=0)


Q1choices = (
    ('0', "No"),
    ('2.75', "Yes"),
)

Q2choices = (
    ('0', "No"),
    ('1.75', "Yes"),
)

Q3choices = (
    ('0', "No"),
    ('2.75', "Yes"),
)

Q4choices = (
    ('0', "No"),
    ('5.50', "Yes"),
)

Q5choices = (
    ('0', "No"),
    ('8', "Yes"),
)

Q6choices = (
    ('0', "No"),
    ('2.7', "Yes"),
)

Q7choices = (
    ('0', "No"),
    ('3.5', "Yes"),
)

Q8choices = (
    ('0', "No"),
    ('8', "Yes"),
)

Q9choices = (
    ('0', "No"),
    ('4.5', "Yes"),
)

Q10choices = (
    ('0', "No"),
    ('5.25', "Yes"),
)

Q11choices = (
    ('0', "No"),
    ('6', "Yes"),
)

Q12choices = (
    ('0', "No"),
    ('7.5', "Yes"),
)


class DasiForm(forms.Form):
    take_care = forms.ChoiceField(label='Take care of yourself, that is, eat, dress, bathe or use the toilet?',
                                  choices=Q1choices, widget=forms.RadioSelect())
    walk_indoors = forms.ChoiceField(label='Walk indoors, such as around your house?', choices=Q2choices,
                                     widget=forms.RadioSelect())
    walk_200 = forms.ChoiceField(label='Walk a block or two on level ground?', choices=Q3choices,
                                 widget=forms.RadioSelect())
    climb_stairs = forms.ChoiceField(label='Climb a flight of stairs or walk up a hill?', choices=Q4choices,
                                     widget=forms.RadioSelect())
    run_short = forms.ChoiceField(label='Run a short distance?', choices=Q5choices, widget=forms.RadioSelect())
    light_work = forms.ChoiceField(label='Do light work around the house like dusting or washing dishes?',
                                   choices=Q6choices, widget=forms.RadioSelect())
    moderate_work = forms.ChoiceField(
        label='Do moderate work around the house like vacuuming, sweeping floors or carrying groceries?',
        choices=Q7choices, widget=forms.RadioSelect())
    heavy_work = forms.ChoiceField(
        label='Do heavy work around the house like scrubbing floors or lifting or moving heavy furniture?',
        choices=Q8choices, widget=forms.RadioSelect())
    yard_work = forms.ChoiceField(label='Do garden work like raking leaves, weeding or pushing a lawn mower?',
                                  choices=Q9choices, widget=forms.RadioSelect())
    sexual_relations = forms.ChoiceField(label='Have sexual relations?', choices=Q10choices, widget=forms.RadioSelect())
    moderate_rec = forms.ChoiceField(
        label='Participate in moderate recreational activities like golf, bowling, dancing, doubles tennis or throwing a ball?',
        choices=Q11choices, widget=forms.RadioSelect())
    strenuous_sports = forms.ChoiceField(
        label='Participate in strenuous sports like swimming, singles tennis, football, basketball or skiing?',
        choices=Q12choices, widget=forms.RadioSelect())
