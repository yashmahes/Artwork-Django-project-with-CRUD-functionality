from django import forms
from .models import Artist
from django import forms


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = "__all__"

# class ArtistForm(forms.Form):
#     Name = forms.CharField(max_length=50, required=True)
#     Birthplace = forms.CharField(max_length=50, required=True)
#     Born = forms.CharField(max_length=50, required=True)
#     Death = forms.CharField(max_length=50, required=True)
#     Movement = forms.CharField(max_length=50, required=True)

    # class Meta:
    #     model = Artist
    #     # fields = ('username', 'first_name', 'last_name',
    #     #           'email', 'password1', 'password2', )
    #     fields = ('title', 'release_year', 'number_in_stock',
    #               'daily_rate', 'genre')
