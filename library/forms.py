from django.forms import ModelForm
from .models import *


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'
        
class MyUserCreationForm(ModelForm):
    username = forms.CharField(max_length=30, required=True, help_text='Required.')
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    # passwords = forms.CharField('')
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
