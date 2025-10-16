from django.contrib import admin
from django.db import models
from students.models import Student, hostel_fee, mess_deposit, fine, Upload
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# from data_importer.importers import XLSImporter
# Register your models here.

class StudentResource(resources.ModelResource):
    class Meta:
        model=Student
        fields = ('usn', 'name', 'email','hostel_fee_paid','mess_bill_paid','fine_student')
        import_id_fields = ['usn','name','email','hostel_fee_paid','mess_bill_paid','fine_student']        
        
@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('usn', 'name', 'email', 'profile_picture_preview')
    list_filter=('name',)
    resource_class= StudentResource
    
    def profile_picture_preview(self, obj):
        if obj.profile_picture:
            return f'<img src="{obj.profile_picture.url}" style="width: 50px; height: 50px; border-radius: 50%; object-fit: cover;">'
        return "No Image"
    profile_picture_preview.allow_tags = True
    profile_picture_preview.short_description = "Profile Picture"

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

# class xlsImporterModel(XLSImporter):
#     fields=['usn','name','email']
#     class Meta:
#         model=Student
    