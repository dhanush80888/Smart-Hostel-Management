import os
import django
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_hostel.settings')
django.setup()

from django.contrib.auth.models import User
from hostel.models import Room, StudentProfile, Complaint, Announcement, MessMenu, WeeklyMenu
from datetime import date, timedelta

# Create admin user
if not User.objects.filter(username='admin').exists():
    admin_user = User.objects.create_superuser(
        username='admin',
        email='admin@hostel.com',
        password='admin123',
        first_name='Admin',
        last_name='User'
    )
    print("✓ Admin user created (username: admin, password: admin123)")
else:
    print("✓ Admin user already exists")
    admin_user = User.objects.get(username='admin')

# Create sample rooms
rooms_data = [
    {'room_no': '101', 'capacity': 4, 'rent': Decimal('5000.00')},
    {'room_no': '102', 'capacity': 4, 'rent': Decimal('5000.00')},
    {'room_no': '103', 'capacity': 4, 'rent': Decimal('5000.00')},
    {'room_no': '201', 'capacity': 4, 'rent': Decimal('5000.00')},
    {'room_no': '202', 'capacity': 4, 'rent': Decimal('5000.00')},
]

for data in rooms_data:
    if not Room.objects.filter(room_no=data['room_no']).exists():
        Room.objects.create(**data)
        print(f"✓ Room {data['room_no']} created")
    else:
        print(f"✓ Room {data['room_no']} already exists")

# Create sample students
students_data = [
    {'username': 'student1', 'email': 'student1@example.com', 'password': 'pass123', 'first_name': 'John', 'last_name': 'Doe', 'roll': 'CS001'},
    {'username': 'student2', 'email': 'student2@example.com', 'password': 'pass123', 'first_name': 'Jane', 'last_name': 'Smith', 'roll': 'CS002'},
    {'username': 'student3', 'email': 'student3@example.com', 'password': 'pass123', 'first_name': 'Bob', 'last_name': 'Johnson', 'roll': 'CS003'},
]

for data in students_data:
    if not User.objects.filter(username=data['username']).exists():
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            first_name=data['first_name'],
            last_name=data['last_name']
        )
        # Update profile with roll number
        profile = user.studentprofile
        profile.roll_number = data['roll']
        profile.fees_due = Decimal('10000.00')
        profile.save()
        print(f"✓ Student {data['username']} created")
    else:
        print(f"✓ Student {data['username']} already exists")

# Allocate rooms to some students
if StudentProfile.objects.filter(room__isnull=True).exists():
    rooms = list(Room.objects.all())
    students = list(StudentProfile.objects.filter(room__isnull=True))
    
    for i, student in enumerate(students[:3]):
        if i < len(rooms):
            student.room = rooms[i]
            student.fees_due = rooms[i].rent * 12  # Annual fees
            student.save()
            print(f"✓ Allocated Room {rooms[i].room_no} to {student.user.username}")

# Create sample complaints
complaint_data = [
    {'title': 'Water leakage in room 101', 'description': 'There is water leaking from the ceiling', 'status': 'open'},
    {'title': 'Internet not working', 'description': 'WiFi connection is unstable', 'status': 'in_progress'},
    {'title': 'Broken window', 'description': 'Window in room 201 is broken', 'status': 'open'},
]

students = list(StudentProfile.objects.all())
if students:
    for i, data in enumerate(complaint_data):
        student = students[i % len(students)]
        if not Complaint.objects.filter(title=data['title']).exists():
            Complaint.objects.create(
                student=student,
                title=data['title'],
                description=data['description'],
                status=data['status']
            )
            print(f"✓ Complaint '{data['title']}' created")
        else:
            print(f"✓ Complaint '{data['title']}' already exists")

# Create sample announcements
announcement_data = [
    {
        'title': 'Hostel Maintenance Schedule',
        'content': 'Electrical maintenance will be conducted on 15th March from 2-5 PM. Power may be interrupted in blocks A and B.',
        'priority': 'high'
    },
    {
        'title': 'New Semester Fee Payment',
        'content': 'Semester fees for the upcoming term are now due. Please complete payment by 20th March to avoid late fees.',
        'priority': 'medium'
    },
    {
        'title': 'Sports Week Announcement',
        'content': 'Inter-hostel sports week will begin from 25th March. Registration for various events is now open.',
        'priority': 'low'
    },
]

if not Announcement.objects.exists():
    for data in announcement_data:
        Announcement.objects.create(
            title=data['title'],
            content=data['content'],
            priority=data['priority'],
            created_by=admin_user
        )
        print(f"✓ Announcement '{data['title']}' created")
else:
    print("✓ Announcements already exist")

# Create sample mess menu for today and next few days
today = date.today()
mess_menu_data = [
    {'date': today, 'meal_type': 'breakfast', 'items': 'Idli, Sambar, Chutney, Coffee, Banana'},
    {'date': today, 'meal_type': 'lunch', 'items': 'Rice, Dal, Mixed Vegetables, Raita, Papad, Pickle'},
    {'date': today, 'meal_type': 'dinner', 'items': 'Chapati, Paneer Curry, Jeera Rice, Salad, Gulab Jamun'},
    {'date': today + timedelta(days=1), 'meal_type': 'breakfast', 'items': 'Poha, Tea, Bread Jam, Orange'},
    {'date': today + timedelta(days=1), 'meal_type': 'lunch', 'items': 'Biryani, Raita, Boondi Raita, Salad'},
    {'date': today + timedelta(days=1), 'meal_type': 'dinner', 'items': 'Dal Rice, Aloo Gobi, Curd, Halwa'},
]

# create a simple weekly menu structure (breakfast/lunch/snacks/dinner) for demo
weekly_data = {
    'monday': ('Oats, Milk', 'Veg Rice, Dal', 'Tea & Snacks', 'Chapati + Sabzi'),
    'tuesday': ('Upma, Juice', 'Curd Rice, Fryums', 'Samosa', 'Roti + Paneer'),
    'wednesday': ('Paratha, Pickle', 'Chole Bhature', 'Biscuits', 'Rice + Dal'),
    'thursday': ('Dosa, Chutney', 'Veg Biryani', 'Tea & Pakoda', 'Chapati + Veg'),
    'friday': ('Bread Omelette', 'Fried Rice', 'Sandwich', 'Roti + Chicken'),
    'saturday': ('Idli', 'Pulao', 'Sweets', 'Roti + Curry'),
    'sunday': ('Poori', 'Khichdi', 'Juice', 'Dinner Special'),
}
try:
    for day, (b, l, s, d) in weekly_data.items():
        obj, created = WeeklyMenu.objects.get_or_create(day=day)
        obj.breakfast = b
        obj.lunch = l
        obj.snacks = s
        obj.dinner = d
        obj.is_active = True
        obj.save()
        if created:
            print(f"✓ WeeklyMenu {day} created")
        else:
            print(f"✓ WeeklyMenu {day} updated")
except Exception as exc:
    print("⚠️  Could not populate weekly menu. Ensure you have run migrations (python manage.py migrate) and the WeeklyMenu table exists.")
    print(exc)
    # continue, other data may still be created

# Add a bit of sample attendance and feedback for the first student (if any)
students = StudentProfile.objects.all()
if students:
    stud = students[0]
    MealAttendance.objects.get_or_create(student=stud, date=today, meal_type='breakfast', defaults={'status': 'taken'})
    FoodFeedback.objects.get_or_create(student=stud, date=today, meal_type='breakfast', defaults={'rating': 4, 'comment': 'Nice breakfast'})
    print(f"✓ Sample attendance and feedback added for {stud.user.username}")

for data in mess_menu_data:
    if not MessMenu.objects.filter(date=data['date'], meal_type=data['meal_type']).exists():
        MessMenu.objects.create(**data)
        print(f"✓ Mess menu for {data['date']} {data['meal_type']} created")
    else:
        print(f"✓ Mess menu for {data['date']} {data['meal_type']} already exists")

print("\n✓ All sample data created successfully!")
print("\nAccess the application:")
print("  - Admin Panel: http://127.0.0.1:8000/admin/ (username: admin, password: admin123)")
print("  - Home: http://127.0.0.1:8000/")
print("  - Login with student account: http://127.0.0.1:8000/accounts/login/")
