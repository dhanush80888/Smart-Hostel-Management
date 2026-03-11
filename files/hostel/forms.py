from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Complaint, Room, OutingPass, StudentProfile

class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    roll_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fees_due = forms.DecimalField(required=False, max_digits=9, decimal_places=2, initial=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('title','description','anonymous')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'rows': '4'})

class ComplaintUpdateForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('status', 'response')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update({'class': 'form-control'})
        self.fields['response'].widget.attrs.update({'class': 'form-control', 'rows': '3'})

class AllocateRoomForm(forms.Form):
    username = forms.CharField(label='Student username', widget=forms.TextInput(attrs={'class': 'form-control'}))

class MutualTransferForm(forms.Form):
    student1 = forms.ModelChoiceField(
        queryset=StudentProfile.objects.filter(room__isnull=False).select_related('user', 'room'),
        label='Student 1',
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Student 1"
    )
    student2 = forms.ModelChoiceField(
        queryset=StudentProfile.objects.filter(room__isnull=False).select_related('user', 'room'),
        label='Student 2',
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Student 2"
    )

class OutingPassForm(forms.ModelForm):
    class Meta:
        model = OutingPass
        fields = ('from_date', 'to_date', 'days_requested', 'reason', 'guardian_email', 'guardian_phone')
        widgets = {
            'from_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'to_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'days_requested': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),
            'guardian_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'guardian_phone': forms.TextInput(attrs={'class': 'form-control'}),
        }