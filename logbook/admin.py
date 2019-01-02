from django.contrib import admin

from logbook.models import Consultation, Procedure, Location, Specialty, Procedure_Class

admin.site.register(Consultation)
admin.site.register(Procedure)
admin.site.register(Location)
admin.site.register(Specialty)
admin.site.register(Procedure_Class)
