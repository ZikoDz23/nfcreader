from django.db import models

class NationalID(models.Model):
    card_uid = models.CharField(max_length=256, unique=True)  # Unique card ID
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    id_number = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return f"ID: {self.id_number}, Name: {self.full_name}"

from django import forms

class MRZForm(forms.Form):
    mrz_data = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        label='Enter MRZ Data'
    )
