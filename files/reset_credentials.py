#!/usr/bin/env python
"""
Verify and reset student credentials
"""

import os
import sys
import django

sys.path.insert(0, r'c:\Users\User\Desktop\files')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_hostel.settings')
django.setup()

from django.contrib.auth.models import User
from hostel.models import StudentProfile

print("\n" + "="*60)
print("CHECKING AND FIXING USER CREDENTIALS")
print("="*60)

# Get all student users
students = ['student1', 'student2', 'student3', 'student4', 'student5']

for username in students:
    try:
        user = User.objects.get(username=username)
        
        # Reset password to pass123
        user.set_password('pass123')
        user.save()
        
        print(f"✅ {username}: Password reset to 'pass123'")
        print(f"   Email: {user.email}")
        print(f"   Active: {user.is_active}")
        
    except User.DoesNotExist:
        print(f"❌ User '{username}' not found")

# Check admin
try:
    admin = User.objects.get(username='admin')
    admin.set_password('admin123')
    admin.save()
    print(f"\n✅ admin: Password set to 'admin123'")
except User.DoesNotExist:
    print(f"\n❌ Admin user not found")

print("\n" + "="*60)
print("✅ CREDENTIALS UPDATED!")
print("="*60)
print("\nYou can now login with:")
print("  Username: student1")
print("  Password: pass123")
print("\nOr as admin:")
print("  Username: admin")
print("  Password: admin123")
print("\n" + "="*60)
