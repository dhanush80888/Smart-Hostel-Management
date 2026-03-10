import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_hostel.settings')
django.setup()

from hostel.models import WeeklyMenu, MealAttendance, FoodFeedback, StudentProfile
from django.contrib.auth.models import User
from django.db import IntegrityError

print("\n" + "="*70)
print("MESS MODULE TEST")
print("="*70 + "\n")

# verify weekly menu days present
try:
    for day, _ in WeeklyMenu.DAYS_OF_WEEK:
        obj, created = WeeklyMenu.objects.get_or_create(day=day, defaults={
            'breakfast': 'Test', 'lunch': 'Test', 'snacks': 'Test', 'dinner': 'Test', 'is_active': True
        })
        print(f"{'Created' if created else 'Found'} menu entry for {day}")
except Exception as e:
    print("⚠️  Could not access WeeklyMenu table - have you run migrations?")
    print(e)
    exit(1)

# create a dummy student if none exists
student = StudentProfile.objects.first()
if not student:
    u = User.objects.create_user(username='testuser', password='testpass')
    student = StudentProfile.objects.create(user=u)
    print("Created test student profile")

# record attendance
today = date.today()
attendance, created = MealAttendance.objects.update_or_create(
    student=student, date=today, meal_type='breakfast',
    defaults={'status': 'taken'}
)
print(f"Attendance recorded: {attendance}")

# try duplicate causing unique constraint
try:
    MealAttendance.objects.create(student=student, date=today, meal_type='breakfast', status='skipped')
except IntegrityError as e:
    print("Unique constraint enforced on MealAttendance")

# submit feedback
fb = FoodFeedback.objects.create(student=student, meal_type='breakfast', rating=4, comment='Good', date=today)
print(f"Feedback saved: {fb}")

print("\n✅ Mess module basic operations appear to work")
print("="*70 + "\n")