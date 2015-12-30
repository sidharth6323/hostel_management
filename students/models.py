from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.

months=(
    ('jan', 'January'),
    ('feb', 'February'),
    ('mar', 'March'),
    ('may', 'April'),
    ('apr', 'May'),
    ('jun', 'June'),
    ('jul', 'July'),
    ('aug', 'August'),
    ('sep', 'September'),
    ('oct', 'October'),
    ('nov', 'November'),
    ('dec', 'December'),
  )

years=(
    ('1st', '1st'),
    ('2nd', '2nd'),
    ('3rd', '3rd'),
    ('4th', '4th'),
  )
    
class mess_deposit(models.Model):
    month=models.CharField(max_length=30,choices=months)
    bill=models.IntegerField()
    
    def __str__(self):
        return '%s (Rs. %s)'%(self.get_month_display(),self.bill)
    
class hostel_fee(models.Model):
    year=models.CharField(max_length=30,choices=years)
    amount=models.IntegerField()
    def __str__(self):
        return '%s (Rs. %s)'%(self.year,self.amount)

class fine(models.Model):
    amount=models.IntegerField()
    reason=models.CharField(max_length=100) 
    def __str__(self):
        return '%s(%s)'%(self.reason,self.amount)
    
class Student(models.Model):
    name=models.CharField(max_length=30)
    usn=models.CharField(max_length=10)
    email=models.EmailField()
    hostel_fee_paid=models.ManyToManyField(hostel_fee,blank=True)
    mess_bill_paid=models.ManyToManyField(mess_deposit,blank=True)
    fine_student=models.ManyToManyField(fine,blank=True)
    
    def __str__(self):
        return '%s(%s)'%(self.name,self.usn)
    class Meta:
        ordering=["usn"]

def validate_file_extension(value):
    if not value.name.endswith('.xls'):
        raise ValidationError(u'Please select an Excel(.xls) file')
    
class Upload(models.Model):
    file=models.FileField("xls",upload_to="files/", validators=[validate_file_extension])
    name=models.CharField(max_length=30,default="tempfile")
    
    def __str__(self):
        return '%s'%(self.name)

