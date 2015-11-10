from django.contrib import admin
from django.http import HttpResponse

from .models import Student, Program_Of_Study

def export_csv(modeladmin, request, queryset):
        import csv
        from django.utils.encoding import smart_str
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=mymodel.csv'
        writer = csv.writer(response, csv.excel)
        response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
        writer.writerow([
            smart_str(u"ID"),
            smart_str(u"Title"),
            smart_str(u"Description"),
        ])
        for obj in queryset:
            writer.writerow([
                smart_str(obj.pk),
                smart_str(obj.student_first_name),
                smart_str(obj.student_last_name),
            ])
        return response
export_csv.short_description = u"Export CSV"


class StudentAdmin(admin.ModelAdmin):
    actions = [export_csv]
    
admin.site.register(Student, StudentAdmin)
admin.site.register(Program_Of_Study)
