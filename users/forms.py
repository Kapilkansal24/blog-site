from django import forms 


class Login(forms.Form):
    email = forms.EmailField(required=True, label="Enter your email ", widget=forms.TextInput(attrs={"placeholder" : "EMAIL : "}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, label="Enter your password")

class Signup(forms.Form):
    firstname = forms.CharField(max_length=70)
    lastname = forms.CharField(max_length=80)
    email = forms.EmailField()
    password = forms.CharField(max_length=40, widget=forms.PasswordInput)
    cpassword = forms.CharField(max_length=40, widget=forms.PasswordInput, label="Confirm Password")
    picture = forms.ImageField()
# email and password will act as a name attribute
class GetEmail(forms.Form):
    email = forms.EmailField(max_length=300)

class Otp(forms.Form):
    otp = forms.CharField(max_length=10)

class ChangePassword(forms.Form):
    password = forms.CharField(max_length=40, widget=forms.PasswordInput)
    cpassword = forms.CharField(max_length=40, widget=forms.PasswordInput, label="Confirm Password")