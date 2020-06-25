from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from ..models import User, Category
from django.core.validators import MinLengthValidator
class SignUpForm(UserCreationForm):
    username = forms.CharField(label="Votre nom d'utilisateur", required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label="Votre adresse email", required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Votre mot de passe", required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Votre confirmation de mot de passe", required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    def clean(self):
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email exists", code="already exist")
       return self.cleaned_data
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("email",)

class LoginForm(forms.Form):
    username = forms.CharField(label="Votre adresse email", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Votre adresse email valide'}))
    password = forms.CharField(label="Votre mot de passe", required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Votre mot de passe'}))

class NewAdForm(forms.Form):
    title = forms.CharField(label="Titre de l'annonce", required=True, widget=forms.TextInput(attrs={'class':'form-control'}), validators=[MinLengthValidator(5,message="Le titre doit faire au minimum %(limit_value)d caractères.")])
    text = forms.CharField(label="Description de votre annonce", required=True, widget=forms.Textarea(attrs={'class':'form-control'}), validators=[MinLengthValidator(20,message="La description doit faire au minimum %(limit_value)d caractères.")])
    price = forms.IntegerField(label="Votre prix", required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True, widget=forms.Select(attrs={'class':'form-control'}))
    file_field = forms.FileField(widget=forms.FileInput(attrs={'multiple': True,'class':'form-control', 'accept':"image/*"}))