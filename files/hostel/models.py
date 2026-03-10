from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from decimal import Decimal

class Room(models.Model):
    room_no = models.CharField(max_length=10, unique=True)
    capacity = models.PositiveIntegerField(default=1)
    rent = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.room_no} (₹{self.rent})"

    @property
    def occupants_count(self):
        return self.studentprofile_set.count()

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=30, blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)
    fees_due = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    fees_paid = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    joined_on = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

    @property
    def outstanding(self):
        if self.fees_due is None:
            return Decimal('0.00')
        return self.fees_due - (self.fees_paid or Decimal('0.00'))

class Payment(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    paid_on = models.DateTimeField(default=timezone.now)
    method = models.CharField(max_length=50, default='offline')

    def __str__(self):
        return f"{self.student} paid ₹{self.amount}"

class Complaint(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    response = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    anonymous = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"

class OutingPass(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    days_requested = models.PositiveIntegerField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    requested_on = models.DateTimeField(auto_now_add=True)
    approved_on = models.DateTimeField(null=True, blank=True)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_passes')
    rejection_reason = models.TextField(blank=True)
    guardian_email = models.EmailField(blank=True)
    guardian_phone = models.CharField(max_length=20, blank=True)
    notification_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"Outing Pass - {self.student} ({self.get_status_display()})"

    class Meta:
        ordering = ['-requested_on']

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    priority = models.CharField(max_length=20, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent')
    ], default='medium')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

class MessMenu(models.Model):
    MEAL_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    ]
    date = models.DateField()
    meal_type = models.CharField(max_length=20, choices=MEAL_CHOICES)
    items = models.TextField(help_text="List of food items separated by commas")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.date} - {self.get_meal_type_display()}"

    class Meta:
        ordering = ['date', 'meal_type']
        unique_together = ['date', 'meal_type']

class Visitor(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    visitor_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    purpose = models.TextField()
    visiting_date = models.DateField()
    expected_entry_time = models.TimeField()
    expected_exit_time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.visitor_name} visiting {self.student}"

    class Meta:
        ordering = ['-created_at']

class VisitorLog(models.Model):
    visitor = models.OneToOneField(Visitor, on_delete=models.CASCADE)
    entry_time = models.DateTimeField(null=True, blank=True)
    exit_time = models.DateTimeField(null=True, blank=True)
    security_staff = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Log for {self.visitor}"

    class Meta:
        ordering = ['-entry_time']

class WeeklyMenu(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]
    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK, unique=True)
    breakfast = models.TextField()
    lunch = models.TextField()
    dinner = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.get_day_display()} Menu"

class MealAttendance(models.Model):
    MEAL_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    ]
    STATUS_CHOICES = [
        ('taken', 'Taken'),
        ('skipped', 'Skipped'),
    ]
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    date = models.DateField()
    meal_type = models.CharField(max_length=10, choices=MEAL_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.student} - {self.get_meal_type_display()} ({self.date})"

    class Meta:
        unique_together = ['student', 'date', 'meal_type']

class FoodFeedback(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.rating} stars"

    class Meta:
        ordering = ['-created_at']

class FoodPoll(models.Model):
    month = models.DateField(help_text="First day of the month")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Poll for {self.month.strftime('%B %Y')}"

    class Meta:
        ordering = ['-month']

class PollOption(models.Model):
    poll = models.ForeignKey(FoodPoll, on_delete=models.CASCADE)
    food_item = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.food_item} ({self.poll})"

    class Meta:
        unique_together = ['poll', 'food_item']

class PollVote(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    poll_option = models.ForeignKey(PollOption, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} voted for {self.poll_option.food_item}"

    class Meta:
        unique_together = ['student', 'poll_option']