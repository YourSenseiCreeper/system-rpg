from django.forms import ModelForm
from .models import Dialogue
ID_CHOICES = [0, 1, 2, 3, 4, 5]


class DialogueForm(ModelForm):
    class Meta:
        model = Dialogue
        fields = '__all__'
    
    answer_one = model.
    # dialogue_id = forms.IntegerField(label = "Unikalne ID dialogu", required = True)
    # location_id = forms.Select(default=0, choices=ID_CHOICES, required = True)
    # answer_nbr = forms.Select(default=0, choices=ID_CHOICES, required = True)
    # access_lvl = forms.IntegerField(label = 'Poziom dostępu', default=0, required = True)
    # character_id = forms.Select(default=0, choices=ID_CHOICES, required = True)
    # narration_id = forms.Select(default=0, choices=ID_CHOICES, required = True)
