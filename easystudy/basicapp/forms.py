from django import forms
from django.contrib.auth.models import User
from basicapp.models import UserProfile

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password','confirm_password')
        help_texts = { 'username': None,}
    def clean(self):
        all_clean_data=super().clean()
        passw=all_clean_data['password']
        rpassw=all_clean_data['confirm_password']
        if len(passw) < 6:
            raise forms.ValidationError("Your password should be at least 6 Characters")
        if passw!= rpassw :
            raise forms.ValidationError("Make sure Password match!!")

class UserProfileForm(forms.ModelForm):
    class Meta():
        model=UserProfile
        fields=('first_name','last_name','phone','street','city','code','state')
