#!/usr/bin/env python
"""
Create test student user for testing outing pass feature
"""

import os
import sys
import django

sys.path.insert(0, r'c:\Users\User\Downloads\files (3)\FILES')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_hostel.settings')
django.setup()

from django.contrib.auth.models import User
from hostel.models import StudentProfile
from decimal import Decimal

print("\n" + "="*60)
print("CREATING TEST USERS")
print("="*60)

# Create 5 test students
students = [
    ('student1', 'pass123', 'Student', 'One', 'CS/2024/001'),
    ('student2', 'pass123', 'Student', 'Two', 'CS/2024/002'),
    ('student3', 'pass123', 'Student', 'Three', 'CS/2024/003'),
    ('student4', 'pass123', 'Student', 'Four', 'CS/2024/004'),
    ('student5', 'pass123', 'Student', 'Five', 'CS/2024/005'),
]

for username, password, first_name, last_name, roll_no in students:
    try:
        # Check if user exists
        if User.objects.filter(username=username).exists():
            print(f"⚠️  User '{username}' already exists - skipping")
            continue
        
        # Create user
        user = User.objects.create_user(
            username=username,
            email=f'{username}@example.com',
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        
        # Create StudentProfile
        profile = StudentProfile.objects.create(
            user=user,
            roll_number=roll_no,
            fees_due=Decimal('5000.00'),
            fees_paid=Decimal('0.00')
        )
        
        print(f"✅ Created: {username} / {password}")
        
    except Exception as e:
        print(f"❌ Error creating {username}: {e}")

# Also create/update admin
try:
    admin_user = User.objects.get(username='admin')
    print(f"✅ Admin user already exists")
except User.DoesNotExist:
    admin_user = User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='admin123'
    )
    print(f"✅ Created admin user: admin / admin123")

print("\n" + "="*60)
print("✅ ALL USERS CREATED SUCCESSFULLY!")
print("="*60)
print("\nTest Credentials:")
print("  Student: student1 / pass123")
print("  Admin:   admin / admin123")
print("\n" + "="*60)
