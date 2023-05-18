from django import forms
from .models import *


class ExhibitionForm(forms.ModelForm):
    class Meta:
        model = Exhibition
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
    )

    class Meta:
        model = Review
        fields = '__all__'
        fields = ('content',)


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'


class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = '__all__'
