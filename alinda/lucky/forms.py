from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.apps import apps

Task = apps.get_model('lucky', 'Task')

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email',
            'maxlength': '254',
        })
    )
    
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Choose a Username',
                'maxlength': '150',
                'pattern': '[a-zA-Z0-9_]+',
                'title': 'Username can only contain letters, numbers, and underscores',
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Password (min 8 characters)',
            'minlength': '8',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm Password',
            'minlength': '8',
        })
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError("Email is required.")
        email = email.lower().strip()
        if len(email) > 254:
            raise ValidationError("Email address is too long.")
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise ValidationError("Username is required.")
        username = username.strip()
        if len(username) < 3:
            raise ValidationError("Username must be at least 3 characters long.")
        if len(username) > 150:
            raise ValidationError("Username is too long (maximum 150 characters).")
        if not username.replace('_', '').replace('-', '').isalnum():
            raise ValidationError("Username can only contain letters, numbers, underscores, and hyphens.")
        if User.objects.filter(username=username).exists():
            raise ValidationError("A user with this username already exists.")
        return username
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# ----------------------------------------------------------------------
# 2. Custom Login Form
# ----------------------------------------------------------------------

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'autocomplete': 'off'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        
        if username and password:
            from django.contrib.auth import authenticate
            user = authenticate(username=username, password=password)
            if user is None:
                raise ValidationError("Invalid username or password. Please try again.")
        return cleaned_data 

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'quantity', 'category', 'price']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter item name (e.g., Milk)',
                'required': True,
                'maxlength': '200',
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'max': '9999',
                'placeholder': 'Qty',
                'required': True
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'max': '999999.99',
                'step': '0.01',
                'placeholder': 'Price',
                'required': True
            })
        }
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise ValidationError("Item name is required.")
        title = title.strip()
        if len(title) < 1:
            raise ValidationError("Item name cannot be empty.")
        if len(title) > 200:
            raise ValidationError("Item name is too long (maximum 200 characters).")
        return title
    
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity is None:
            raise ValidationError("Quantity is required.")
        if quantity < 1:
            raise ValidationError("Quantity must be at least 1.")
        if quantity > 9999:
            raise ValidationError("Quantity is too large (maximum 9999).")
        return quantity
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None:
            raise ValidationError("Price is required.")
        if price < 0:
            raise ValidationError("Price cannot be negative.")
        if price > 999999.99:
            raise ValidationError("Price is too large (maximum $999,999.99).")
        return price