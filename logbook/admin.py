from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from logbook.models import Consultation, Procedure, Location, Specialty, Procedure_Class


class ConsultationResource(resources.ModelResource):
    class Meta:
        model = Consultation

class ConsultationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ConsultationResource
    fields = [('uid', 'name'), ('date_of_birth', 'sex'), ('date_of_contact', 'location', 'post_code'), ('specialty', 'diagnosis'), ('supervision', 'sentiment'), 'notes']


class ProcedureResource(resources.ModelResource):
    class Meta:
        model = Procedure


class ProcedureAdmin(ImportExportModelAdmin):
    resource_class = ProcedureResource


admin.site.register(Consultation, ConsultationAdmin)
admin.site.register(Procedure, ProcedureAdmin)
admin.site.register(Location)
admin.site.register(Specialty)
admin.site.register(Procedure_Class)