from dal import autocomplete

from django import forms

from api.models.mass_models import Mass


class PersonForm(forms.ModelForm):
    class Meta:
        model = Mass
        fields = ('__all__')
        widgets = {
            'mass_moments': autocomplete.ModelSelect2Multiple(url='mass-moments-autocomplete')
        }
