import datetime

from django import forms



class GameForm(forms.Form):
    game_choice = forms.ChoiceField(choices=[('coin','монетка'), ('cube','бросить кубик'),])
    tries = forms.IntegerField(min_value=1, max_value=10)

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    description = forms.CharField(widget=forms.Textarea)
    bday = forms.DateField(initial=datetime.date.today,widget=forms.DateInput(attrs={'class': 'form-control', 'type':'date'}))