import csv
import os

path = "/home/nrsmoll/Dropbox/PyProjects/Homepage/static/data"  # Set path of new directory here
os.chdir(path)  # changes the directory

from logbook.models import Location  # imports the model

with open('locations.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = Location(location=row['Locations'])
        p.save()

from logbook.models import Specialty  # imports the model

with open('specialties.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = Specialty(specialty=row['specialty'])
        p.save()

from logbook.models import Consultation  # imports the model

with open('master20190103.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = Consultation(uid=row['MRN'], name=row['Name'], location_id=row['Hospital'],
                         date_of_contact=row['Date_of_Encounter'], sex=row['sex'],
                         date_of_birth=row['date_of_birth'], specialty_id=row['category'], diagnosis=row['Diagnosis'],
                         supervision=row['Supervision'], notes=row['notes'], post_code=row['post_code'])
        p.save()

from logbook.models import Procedure  # imports the model

with open('proceduremaster_20190103.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = Procedure(uid=row['URN'], name=row['Name'], location_id=row['location'],
                      date_of_contact=row['procedure_date'], procedure_name=row['procedure'],
                      procedure_class_id=row['type_of_procedure'],
                      date_of_birth=row['dob'], specialty_id=row['specialty'], sex=row['sex'],
                      supervision=row['supervision'])
        p.save()
