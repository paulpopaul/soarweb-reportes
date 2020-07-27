from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(label='first_name ', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'TU NOMBRE'}
    ))

    last_name = forms.CharField(label='last_name', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'APELLIDO'}
    ))

    phone = forms.CharField(label='phone', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'TELEFONO'}
    ))

    email = forms.EmailField(label='email', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'EMAIL'}
    ))

    message = forms.CharField(widget=forms.Textarea(
        attrs={'cols': '5', 'rows': '10', 'class': 'form-control', 'placeholder': 'MENSAJE'}
    ))

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'phone', 'message')

        # this function will be used for the validation 
    '''def clean(self): 
  
        # data from the form is fetched using super function 
        super(ContactForm, self).clean() 
          
        # extract the username and text field from the data 
        first_name = self.cleaned_data.get('first_name') 
        last_name = self.cleaned_data.get('last_name') 
  
        # conditions to be met for the username length 
        if len(first_name) < 5: 
            self._errors['first_name'] = self.error_class([ 
                'Minimum 5 characters required']) 
        if len(last_name) <10: 
            self._errors['last_name'] = self.error_class([ 
                'Post Should Contain minimum 10 characters']) 
  
        # return any errors if found 
        return self.cleaned_data '''