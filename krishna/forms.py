from django import forms
from .models import Register,File,Push

class RegisterDataForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ["name", "age", "address", "mail"]

        
class upload(forms.ModelForm):
    class Meta:
        model = File
        fields = ["filename","myfile"]
        
class pushupload(forms.ModelForm):
    class Meta:
        model = Push
        fields = ["title","description","publish"]       
               



      
