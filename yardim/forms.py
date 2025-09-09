
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Category, HelpRequest, Profile, Comment, Message  # Message modeli eklendi

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="E-posta")
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES, label="Kullanıcı Rolü")

    class Meta:
        model = User
        fields = ("username", "email", "role")

class HelpRequestForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label="Kategori")
    title = forms.CharField(max_length=200, label="Başlık")
    description = forms.CharField(widget=forms.Textarea, label="Açıklama")
    help_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Yardım Tarihi",
        required=False
    )
    location = forms.CharField(
        max_length=255,
        label="Konum",
        required=False
    )
    is_urgent = forms.BooleanField(
        label="Acil İlan",
        required=False
    )

    class Meta:
        model = HelpRequest
        fields = ('category', 'title', 'description', 'help_date', 'location', 'is_urgent')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['role', 'bio', 'location', 'phone_number', 'profile_picture']
        labels = {
            'role': 'Rol',
            'bio': 'Biyografi',
            'location': 'Konum',
            'phone_number': 'Telefon Numarası',
            'profile_picture': 'Profil Fotoğrafı'
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content': 'Yorumunuz'}

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'content']
        labels = {
            'receiver': 'Alıcı',
            'content': 'Mesajınız'
        }

