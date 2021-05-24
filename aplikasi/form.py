from django.forms import ModelForm
from aplikasi.models import *
from django import forms

class FormKaryawan(ModelForm):
    class Meta:
        model = Karyawan
        fields = '__all__'

        widgets={
            'nama' : forms.TextInput({'class': 'form-control'}),
            'masa_kerja': forms.NumberInput({'class': 'form-control'}),
            'usia': forms.NumberInput({'class': 'form-control'}),
            'prestasi': forms.Select({'class': 'form-control'}),
            'kemampuan_komunikasi': forms.Select({'class': 'form-control'}),
            'kesehatan': forms.Select({'class': 'form-control'}),
        }