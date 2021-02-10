"""Contact App Forms."""
from django import forms
from offer.models import Offer


class ContactForm(forms.Form):
    """Contact Form."""
    name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=False)
    offer = forms.ModelChoiceField(queryset=Offer.objects.all().order_by('name'))
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        """This function will add placeholders and classes and set autofocus on
        name field."""
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'from_email': 'Email Address',
            'subject': 'Subject',
            'offer': 'Offer',
            'message': 'Message',
        }

        # Change number of visible rows in textarea field
        self.fields['message'].widget.attrs = {'rows': 5}
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field == 'offer':
                self.fields['offer'].required = False
            else:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
            self.fields['offer'].empty_label = 'Select offer, if related'
