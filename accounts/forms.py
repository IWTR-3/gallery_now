from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms

# 회원가입폼 위젯
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label='이메일',
        widget=forms.TextInput(
            attrs={'class': 'form-control','placeholder': '이메일을 입력하세요',}),)
    nickname = forms.CharField(
        label='닉네임',
        widget= forms.TextInput(
            attrs={'class': 'form-control','placeholder': '닉네임을 입력하세요',}))
    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control','placeholder': '비밀번호를 입력하세요',}),)
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control','placeholder': '비밀번호를 다시 입력하세요',}),)    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email', 'nickname') 


# 로그인폼 위젯 
class LogInForm(AuthenticationForm):
    email = forms.EmailField(
        label='이메일',
        widget=forms.TextInput(
            attrs={'class': 'form-control','placeholder': '이메일을 입력하세요',}),)
    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control','placeholder': '비밀번호를 입력하세요',}),)
    class Meta:
        model = get_user_model()
        fields = ('password',)
