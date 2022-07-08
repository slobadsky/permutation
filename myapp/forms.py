from django import forms
from .models import Permutation
from django.contrib.auth.models import User

class damndePermutForm(forms.ModelForm):
    class Meta:
        model = Permutation
        fields = ['permut_start_datetime',
                  'permut_end_time',
                  'permut_acceptant_start_datetime',
                  'permut_acceptant_end_time',
                  'permut_acceptant',
                  'permut_motif',
                  'permut_accepted',
        ]
        
    permut_start_datetime=forms.DateTimeField(
    required=True,
    widget=forms.NumberInput(attrs={
        'class': "form-control",
        'placeholder': 'Date Heure',
        'type':'datetime-local',
        }))
    
    permut_end_time=forms.TimeField(
        required=True,
        widget=forms.NumberInput(attrs={
        'class': "form-control",
        'placeholder': 'Date Heure',
        'type':'time',
        }))
    
    permut_acceptant_start_datetime=forms.DateTimeField(
    required=True,
    widget=forms.NumberInput(attrs={
        'class': "form-control",
        'placeholder': 'Date Heure',
        'type':'datetime-local',
        }))
    
    permut_acceptant= forms.ModelChoiceField(
        queryset=User.objects.exclude(username= u'admin'),
        empty_label="--- À choisir ---",
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-select',        
                })
        )
    
    permut_acceptant_end_time=forms.TimeField(
        required=True,
        widget=forms.NumberInput(attrs={
        'class': "form-control",
        'placeholder': 'Date Heure',
        'type':'time',
        }))
    
    permut_motif=forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder': 'Vol',
            'type':'text',
            'maxlength':255,
            }))
    
    """permut_accepted=forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={
            'class':'form-check-input',
            'type':'checkbox',
            'value':'False',
            }))"""


   