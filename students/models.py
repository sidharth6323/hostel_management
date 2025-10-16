from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image
import os


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

def validate_image_extension(value):
    allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    ext = os.path.splitext(value.name)[1].lower()
    if ext not in allowed_extensions:
        raise ValidationError(u'Please select a valid image file (JPG, JPEG, PNG, GIF)')

def validate_image_size(value):
    # Limit file size to 5MB
    if value.size > 5 * 1024 * 1024:
        raise ValidationError(u'Image file too large. Size should not exceed 5MB.')

def validate_file_extension(value):
    if not value.name.endswith('.xls'):
        raise ValidationError(u'Please select an Excel(.xls) file')
    
class Student(models.Model):
    name=models.CharField(max_length=30)
    usn=models.CharField(max_length=10)
    email=models.EmailField()
    profile_picture=models.ImageField(upload_to='profile_pics/', blank=True, null=True, 
                                    validators=[validate_image_extension, validate_image_size])
    hostel_fee_paid=models.ManyToManyField(hostel_fee,blank=True)
    mess_bill_paid=models.ManyToManyField(mess_deposit,blank=True)
    fine_student=models.ManyToManyField(fine,blank=True)
    
    def __str__(self):
        return '%s(%s)'%(self.name,self.usn)
    
    def save(self, *args, **kwargs):
        super(Student, self).save(*args, **kwargs)
        
        # Resize image if it exists
        if self.profile_picture:
            try:
                img = Image.open(self.profile_picture.path)
                if img.height > 300 or img.width > 300:
                    output_size = (300, 300)
                    img.thumbnail(output_size, Image.Resampling.LANCZOS)
                    img.save(self.profile_picture.path)
            except Exception as e:
                # If image processing fails, continue without error
                pass
    
    class Meta:
        ordering=["usn"]
    
class Upload(models.Model):
    file=models.FileField("xls",upload_to="files/", validators=[validate_file_extension])
    name=models.CharField(max_length=30,default="tempfile")
    
    def __str__(self):
        return '%s'%(self.name)

