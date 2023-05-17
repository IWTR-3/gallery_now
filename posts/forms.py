from django import forms
from .models import Exhibition, Review, Artist, Gallery


class ExhibitionForm(forms.ModelForm):
    class Meta:
        model = Exhibition
        fields = '__all__'


class ReviewForm(forms.ModelForm):
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
