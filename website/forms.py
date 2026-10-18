
from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control contact-input",
            "placeholder": "First Name",
            "autocomplete": "given-name",
        }),
    )

    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control contact-input",
            "placeholder": "Last Name",
            "autocomplete": "family-name",
        }),
    )

    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={
            "class": "form-control contact-input",
            "placeholder": "Email",
            "autocomplete": "email",
        }),
    )

    phone = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control contact-input",
            "placeholder": "Phone",
            "autocomplete": "tel",
        }),
    )

    message = forms.CharField(
        max_length=5000,
        widget=forms.Textarea(attrs={
            "class": "form-control contact-input contact-message",
            "placeholder": "Type your message here",
            "rows": 5,
        }),
    )

    # Simple honeypot field to help catch basic automated spam.
    website = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "tabindex": "-1",
            "autocomplete": "off",
            "class": "visually-hidden",
        }),
    )

    def clean_website(self):
        value = self.cleaned_data.get("website", "")
        if value:
            raise forms.ValidationError("Invalid submission.")
        return value
