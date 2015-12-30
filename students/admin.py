from django.contrib import admin
from django.db import models
from students.models import Student, hostel_fee, mess_deposit, fine, Upload
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from data_importer.importers import XLSImporter
# Register your models here.

class StudentResource(resources.ModelResource):
    class Meta:
        model=Student
        fields = ('usn', 'name', 'email','hostel_fee_paid','mess_bill_paid','fine_student')
        import_id_fields = ['usn','name','email','hostel_fee_paid','mess_bill_paid','fine_student']        
        
@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_filter=('name',)
    resource_class= StudentResource

@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    pass
  
    
@admin.register(hostel_fee)
class hostel_feeAdmin(admin.ModelAdmin):
    pass
    
@admin.register(mess_deposit)
class mess_depositAdmin(admin.ModelAdmin):
    pass

@admin.register(fine)
class fineAdmin(admin.ModelAdmin):
    pass

class xlsImporterModel(XLSImporter):
    fields=['usn','name','email']
    class Meta:
        model=Student
    