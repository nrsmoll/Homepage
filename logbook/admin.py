from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
import csv
from django.http import HttpResponse

from logbook.models import Consultation, Procedure, Location, Specialty, Procedure_Class


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"



class ConsultationResource(resources.ModelResource):
    class Meta:
        model = Consultation

class ConsultationAdmin(ImportExportModelAdmin, admin.ModelAdmin, ExportCsvMixin):
    resource_class = ConsultationResource
    fields = [('uid', 'name'), ('date_of_birth', 'sex'), ('date_of_contact', 'location'), 'post_code', ('specialty', 'diagnosis'), 'supervision', 'sentiment', 'notes']
    list_display = ('name', 'date_of_birth', 'date_of_contact', 'diagnosis', 'sentiment')
    list_filter = ('specialty', 'date_of_contact', 'supervision')
    actions = ["export_as_csv"]


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