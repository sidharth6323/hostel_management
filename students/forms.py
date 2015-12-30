from models import Student, mess_deposit, hostel_fee, Upload
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields=['email','hostel_fee_paid','mess_bill_paid','fine_student',]
        widgets={'email':forms.TextInput(attrs={'placeholder':'Email','name':'Name','class':'mdl-textfield__input','size': '10'}),
            'hostel_fee_paid':forms.CheckboxSelectMultiple(attrs={'class':'"mdl-checkbox__input'}),
                 'mess_bill_paid':forms.CheckboxSelectMultiple,
                 'fine_student':forms.CheckboxSelectMultiple
                 
                 }

class mess_depositForm(forms.ModelForm):
    class Meta:
        model= mess_deposit
        fields=['month','bill']
        
class hostel_feeForm(forms.ModelForm):
    class Meta:
        model= hostel_fee
        fields=['year','amount']
        
    #code

class signupform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password','is_staff']
        widgets={
            'password':forms.PasswordInput(),
            
        }
        #code
    
class UploadForm(forms.ModelForm):
    class Meta:
        model= Upload
        fields=["file"]