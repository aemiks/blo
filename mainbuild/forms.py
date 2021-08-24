from django import forms
from .models import MyBuildDescription, MyBuild
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    username = forms.CharField(label="Login:", max_length=30, widget=forms.TextInput(attrs={'class': 'username_register first', }))
    email = forms.EmailField(label="Email:",widget=forms.TextInput(attrs={'class': 'username_register'}))
    password = forms.CharField(label='Hasło:', widget=forms.PasswordInput(attrs={'class': 'username_register'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class MyBuildForm(forms.ModelForm):
    """Main build form"""
    class Meta:
        model = MyBuild
        fields = ["name", "image", 'budget']

class MyBuildFormEdit(forms.ModelForm):
    """Main build form"""
    class Meta:
        model = MyBuild
        fields = ["image", "budget"]

class MyBuildDescriptionForm(forms.ModelForm):
    """Building info form"""
    class Meta:
        model = MyBuildDescription
        fields = "__all__"
