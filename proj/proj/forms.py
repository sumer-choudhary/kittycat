from django import forms
from django.forms import fields
from django.contrib.auth import authenticate



class Register(forms.Form):
    name=forms.CharField(max_length=50,label="User",widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Name"}))
    email=forms.EmailField(max_length=50,label="Email",widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter Mail"}))
    password=forms.CharField(max_length=50,label="Password",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password"}))
    rpassword=forms.CharField(max_length=50,label="Re-Password",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm Password"}))

class Login(forms.Form):
    email=forms.EmailField(max_length=50,label="Email",widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter Email"}))
    password=forms.CharField(max_length=50,label="Password",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter password"}))

    # def clean(self, *args, **kwargs):
    #     email=self.cleaned_data.get('email')
    #     password=self.cleaned_data.get('password')

    #     if email and password:
    #         user=authenticate(email=email, password=password)
    #         if not user:
    #             raise forms.ValidationError('this user does not exists')
    #         if not user.check_password(password):
    #             raise forms.ValidationError('incorrect password')
    #         if not user.is_active:
    #             raise forms.ValidationError('this user is not active')
    #     return super(Login,self).clean(*args,**kwargs)
















# def clean(self):
#     cleaned_data = super().clean()
#     valpwd = self.cleaned_data['password']
#     valrpwd = self.cleaned_data['rpassword']
#     if valpwd != valrpwd:
#         raise forms.ValidationError('password does not match')