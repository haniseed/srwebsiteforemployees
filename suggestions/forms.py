from django import forms

from . import models


class GetSelections(forms.ModelForm):
    class Meta:
        model = models.Method
        fields = ['name']
        """
        fields = ['height']
        fields = ['weight']
        fields = ['age']
        fields = ['occupation']
        fields = ['height']
        fields = ['name']
        fields = ['number of working hours']
        """