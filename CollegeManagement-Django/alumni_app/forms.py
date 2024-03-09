
from django import forms
from alumni_app . models import Registration # Import your registration model

class AlumniRegistrationForm(forms.ModelForm):

    class Meta:
        model = Registration  # Specify the registration model
        fields = ['first_name', 'last_name', 'profile_pic','address','gender','rollno', 'graduation_year',
         'major', 'current_employer','current_job_title', 'contact', 'email','password']


# alumini_login

from django import forms
from .models import Registration  # Import your Registration model

class CustomLoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        # Check if the email and password match a Registration object
        try:
            registration_entry = Registration.objects.get(email=email, password=password)
        except Registration.DoesNotExist:
            raise forms.ValidationError("Invalid credentials. Please try again.")

        # You can add additional checks here if needed

        return cleaned_data
