from django import forms

class Contactformemail(forms.Form):
    name = forms.CharField(label='Full Name' ,
                           widget=forms.TextInput(attrs={
                               'placeholder':'Full name',
                               'class':'form-handle my-input',
                           })
                           )
    fromemail=forms.EmailField(required=True)
    subject=forms.CharField(required=True)
    message = forms.CharField(min_length=5, max_length=50, 
                              widget=forms.Textarea(attrs={
                                  'cols':20,
                                  'rows':6,
                                  'placeholder':'Write your message here.....'
                              }))