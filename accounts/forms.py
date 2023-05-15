from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.forms.widgets import ClearableFileInput
from imagekit.forms import ProcessedImageField
from imagekit.processors import ResizeToFill

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email', 'nickname',) 


class CustomUserChangeForm(UserChangeForm):
    profile_image = ProcessedImageField(
        spec_id='profile_image_thumbnail',
        processors=[ResizeToFill(70,70)],
        format='JPEG',
        options={'quality' : 90},
        required=False,
        widget=ClearableFileInput(
        attrs={
        }
        ),
    )
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'nickname', 'profile_image',)
        