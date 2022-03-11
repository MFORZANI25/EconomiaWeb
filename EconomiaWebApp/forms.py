
from django import forms

class FormularioContacto(forms.Form):
    de= forms.EmailField(label="De", required=True)
    para= forms.EmailField(label="Para", required=True)
    mensaje= forms.CharField(label="Mensaje", required=True)
