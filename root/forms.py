from .models import *
from django.forms import ModelForm

class contactform(ModelForm):
    class Meta:
        model=contact
        fields = "__all__"