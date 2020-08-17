from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre",
                           required=True,
                           max_length=100, min_length=3,
                           widget=forms.TextInput(attrs={
                            'class': 'form-control',
                            'placeholder': 'Hola mi amor te quiero'}))

    email = forms.EmailField(label="Email",
                             required=True,
                             max_length=100, min_length=3,
                             widget=forms.EmailInput(attrs={
                              'class': 'form-control',
                              'placeholder': 'Escribe tu Email'}))

    content = forms.CharField(label="Contenido",
                              required=True,
                              max_length=1000, min_length=10,
                              widget=forms.Textarea(attrs={
                               'class': 'form-control',
                               'rows': 3,
                               'placeholder': 'Escribe tu Mensaje'}))
