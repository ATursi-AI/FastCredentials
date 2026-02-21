from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class CertificateSignupForm(UserCreationForm):
    # Removed First/Last Name fields as requested
    email = forms.EmailField(required=True, label="Email Address (User Name)")

    class Meta:
        model = User
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists() or User.objects.filter(username=email).exists():
            raise ValidationError("This email is already registered. Please log in instead.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        # Removed name saving logic since fields are gone
        
        if commit:
            user.save()
        return user
