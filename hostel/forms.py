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


# --- Mess management forms -------------------------------------------------
from .models import WeeklyMenu, MealAttendance, FoodFeedback, Announcement, MaintenanceRequest, EmergencyAlert, LeaveRequest, LostItem, StudentID, ElectricityUsage

class WeeklyMenuForm(forms.ModelForm):
    class Meta:
        model = WeeklyMenu
        fields = ['day', 'breakfast', 'lunch', 'snacks', 'dinner', 'is_active']
        widgets = {
            'day': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'breakfast': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'lunch': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'snacks': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'dinner': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

# ---- forms for new features ----

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'message', 'category', 'expiry_date', 'attachment', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'attachment': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class MaintenanceRequestForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRequest
        fields = ['room_number', 'issue_type', 'description', 'image']
        widgets = {
            'room_number': forms.TextInput(attrs={'class': 'form-control'}),
            'issue_type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class EmergencyAlertForm(forms.ModelForm):
    class Meta:
        model = EmergencyAlert
        fields = ['alert_type', 'message']
        widgets = {
            'alert_type': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['start_date', 'end_date', 'reason', 'parent_email']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'parent_email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class LostItemForm(forms.ModelForm):
    class Meta:
        model = LostItem
        fields = ['item_name', 'description', 'image', 'location']
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }

# additional forms (StudentID creation handled automatically, ElectricityUsage may be admin only)

class ElectricityUsageForm(forms.ModelForm):
    class Meta:
        model = ElectricityUsage
        fields = ['room_number', 'month', 'units_consumed']
        widgets = {
            'room_number': forms.TextInput(attrs={'class': 'form-control'}),
            'month': forms.DateInput(attrs={'type': 'month', 'class': 'form-control'}),
            'units_consumed': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class MealAttendanceForm(forms.ModelForm):
    class Meta:
        model = MealAttendance
        fields = ['meal_type', 'status']
        widgets = {
            'meal_type': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class FoodFeedbackForm(forms.ModelForm):
    class Meta:
        model = FoodFeedback
        fields = ['meal_type', 'rating', 'comment']
        widgets = {
            'meal_type': forms.Select(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }