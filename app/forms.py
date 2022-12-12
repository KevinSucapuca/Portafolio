from django import forms
from .models import Contacto,Portafolio
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):
    
    
    class Meta:
        model = Contacto
        #fields = ["nombre","correo",]
        fields = '__all__'
        


class PortafolioForm(forms.ModelForm):
    
    foto = forms.ImageField(required=False)
    titulo =forms.CharField(min_length=3, max_length=79)
    tags =forms.CharField(min_length=3, max_length=70)
    url = forms.URLField(label='Your website', required=False)
    class Meta:
        model = Portafolio
        fields = '__all__'
        
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'first_name', 'last_name','email','password1','password2']
        
    
