from django import forms
from .models import Pitchingdata

class PostForm(forms.ModelForm):

    class Meta:
        model = Pitchingdata
        fields = ('balltype','batter',)

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
