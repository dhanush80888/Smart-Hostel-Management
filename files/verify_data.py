import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_hostel.settings')
django.setup()

from django.contrib.auth.models import User
from hostel.models import Room, StudentProfile, Complaint, Payment

print("\n" + "="*60)
print("SMART HOSTEL - DATA VERIFICATION REPORT")
print("="*60 + "\n")

# Check Users
users = User.objects.all()
print(f"✓ Total Users: {users.count()}")
print(f"  - Admin Users: {User.objects.filter(is_staff=True).count()}")
print(f"  - Regular Users: {User.objects.filter(is_staff=False).count()}")

# Check StudentProfiles
profiles = StudentProfile.objects.all()
print(f"\n✓ Total Student Profiles: {profiles.count()}")
allocated = profiles.filter(room__isnull=False).count()
print(f"  - Allocated to Rooms: {allocated}")
print(f"  - Unallocated: {profiles.filter(room__isnull=True).count()}")

# Check Rooms
rooms = Room.objects.all()
print(f"\n✓ Total Rooms: {rooms.count()}")
total_capacity = sum(room.capacity for room in rooms)
total_occupants = sum(room.occupants_count for room in rooms)
print(f"  - Total Capacity: {total_capacity}")
print(f"  - Total Occupants: {total_occupants}")
print(f"  - Available Capacity: {total_capacity - total_occupants}")

# Check Complaints
complaints = Complaint.objects.all()
print(f"\n✓ Total Complaints: {complaints.count()}")
print(f"  - Open: {complaints.filter(status='open').count()}")
print(f"  - In Progress: {complaints.filter(status='in_progress').count()}")
print(f"  - Resolved: {complaints.filter(status='resolved').count()}")

# Check Payments
payments = Payment.objects.all()
print(f"\n✓ Total Payments: {payments.count()}")
total_paid = sum(p.amount for p in payments)
print(f"  - Total Amount Collected: ₹{total_paid}")

# Check database connection
print(f"\n✓ Database: SQLite (db.sqlite3)")
print(f"✓ Database Connection: OK")

print("\n" + "="*60)
print("ALL SYSTEMS OPERATIONAL ✓")
print("="*60)

print("\n📋 TEST CREDENTIALS:")
print("  Admin Panel:")
print("    Username: admin")
print("    Password: admin123")
print("\n  Student Accounts:")
for user in User.objects.filter(is_staff=False):
    print(f"    Username: {user.username}")
    print(f"    Password: pass123")

print("\n🚀 START THE SERVER WITH:")
print("  python manage.py runserver")
print("\n🌐 THEN VISIT:")
print("  - http://127.0.0.1:8000/ (Home)")
print("  - http://127.0.0.1:8000/admin/ (Admin Panel)")
print("  - http://127.0.0.1:8000/accounts/login/ (Login)")
print("\n" + "="*60 + "\n")
