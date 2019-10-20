from django import forms
from .models import Pitchingdata

class PostForm(forms.ModelForm):

    class Meta:
        model = Pitchingdata
        fields = ('batter',)
