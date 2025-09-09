from django import forms
from .models import GeeksModel  # Make sure to import your model

class GeeksForm(forms.ModelForm):
    # Specify the name of the model to use
    class Meta:
        model = GeeksModel
        fields = "__all__"
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        # Validate the email format
        if email and not email.endswith('@example.com'):
            raise forms.ValidationError("Please use an email with '@example.com'.")
        
        return email
