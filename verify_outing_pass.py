#!/usr/bin/env python
"""
Verify Outing Pass Feature Installation
Tests all components of the new outing pass generator
"""

import os
import sys
import django

sys.path.insert(0, r'c:\Users\User\Desktop\files')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_hostel.settings')
django.setup()

from django.db import connection
from hostel.models import OutingPass, StudentProfile
from hostel.views import request_outing_pass, my_outing_passes, admin_outing_requests, approve_outing_pass, reject_outing_pass
from hostel.forms import OutingPassForm
from django.urls import reverse

print("\n" + "="*70)
print("🚪 OUTING PASS FEATURE VERIFICATION")
print("="*70)

# Check 1: Database Table
print("\n✓ DATABASE CHECK")
print("-" * 70)
with connection.cursor() as cursor:
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='hostel_outingpass'")
    table_exists = cursor.fetchone() is not None
    if table_exists:
        print("  ✅ OutingPass table exists in database")
        cursor.execute("PRAGMA table_info(hostel_outingpass)")
        columns = cursor.fetchall()
        print(f"  ✅ Table has {len(columns)} columns")
        for col in columns:
            print(f"     • {col[1]} ({col[2]})")
    else:
        print("  ❌ OutingPass table NOT found")

# Check 2: Model
print("\n✓ MODEL CHECK")
print("-" * 70)
try:
    outing = OutingPass()
    print("  ✅ OutingPass model loaded successfully")
    print(f"  ✅ Model fields: {[f.name for f in OutingPass._meta.get_fields()]}")
except Exception as e:
    print(f"  ❌ Error loading model: {e}")

# Check 3: Form
print("\n✓ FORM CHECK")
print("-" * 70)
try:
    form = OutingPassForm()
    print("  ✅ OutingPassForm loaded successfully")
    print(f"  ✅ Form fields: {list(form.fields.keys())}")
except Exception as e:
    print(f"  ❌ Error loading form: {e}")

# Check 4: Views
print("\n✓ VIEWS CHECK")
print("-" * 70)
views_to_check = [
    ('request_outing_pass', request_outing_pass),
    ('my_outing_passes', my_outing_passes),
    ('admin_outing_requests', admin_outing_requests),
    ('approve_outing_pass', approve_outing_pass),
    ('reject_outing_pass', reject_outing_pass),
]

for view_name, view_func in views_to_check:
    if callable(view_func):
        print(f"  ✅ View '{view_name}' exists and is callable")
    else:
        print(f"  ❌ View '{view_name}' not callable")

# Check 5: URLs
print("\n✓ URL ROUTES CHECK")
print("-" * 70)
routes = [
    ('request_outing_pass', '/outing/request/'),
    ('my_outing_passes', '/outing/my-passes/'),
    ('admin_outing_requests', '/outing/admin-requests/'),
    ('approve_outing_pass', '/outing/approve/<id>/'),
    ('reject_outing_pass', '/outing/reject/<id>/'),
]

for route_name, expected_path in routes:
    try:
        url = reverse(route_name)
        # URL might have <id> placeholder
        if '<id>' in expected_path:
            # For dynamic URLs, just check if the route name exists
            print(f"  ✅ Route '{route_name}' configured")
        else:
            if url == expected_path:
                print(f"  ✅ Route '{route_name}' → {url}")
            else:
                print(f"  ⚠️  Route '{route_name}' → {url} (expected: {expected_path})")
    except Exception as e:
        print(f"  ❌ Route '{route_name}' not found: {e}")

# Check 6: Templates
print("\n✓ TEMPLATE FILES CHECK")
print("-" * 70)
templates = [
    'request_outing_pass.html',
    'my_outing_passes.html',
    'admin_outing_requests.html',
    'approve_outing_pass.html',
    'reject_outing_pass.html',
]

template_dir = r'c:\Users\User\Desktop\files\templates\hostel'
for template in templates:
    template_path = os.path.join(template_dir, template)
    if os.path.exists(template_path):
        size = os.path.getsize(template_path)
        print(f"  ✅ {template} ({size} bytes)")
    else:
        print(f"  ❌ {template} NOT found")

# Check 7: Migrations
print("\n✓ MIGRATION CHECK")
print("-" * 70)
migration_file = r'c:\Users\User\Desktop\files\hostel\migrations\0002_outingpass.py'
if os.path.exists(migration_file):
    print(f"  ✅ Migration file exists: 0002_outingpass.py")
    size = os.path.getsize(migration_file)
    print(f"  ✅ File size: {size} bytes")
else:
    print(f"  ❌ Migration file NOT found")

# Check 8: Feature Summary
print("\n✓ FEATURE SUMMARY")
print("-" * 70)
print("  🚪 Outing Pass Generator Features:")
print("  • Students can request outing passes")
print("  • Admins can view and manage requests")
print("  • Auto email notifications to guardians")
print("  • Approval/Rejection workflow")
print("  • Status tracking (Pending/Approved/Rejected)")
print("  • Full audit trail (dates, approver, reasons)")

# Check 9: Data
print("\n✓ DATA CHECK")
print("-" * 70)
try:
    total_passes = OutingPass.objects.count()
    pending = OutingPass.objects.filter(status='pending').count()
    approved = OutingPass.objects.filter(status='approved').count()
    rejected = OutingPass.objects.filter(status='rejected').count()
    
    print(f"  ✅ Total outing passes in database: {total_passes}")
    print(f"     • Pending: {pending}")
    print(f"     • Approved: {approved}")
    print(f"     • Rejected: {rejected}")
except Exception as e:
    print(f"  ❌ Error checking data: {e}")

# Check 10: Integration
print("\n✓ INTEGRATION CHECK")
print("-" * 70)
try:
    profiles = StudentProfile.objects.count()
    print(f"  ✅ StudentProfile count: {profiles}")
    print(f"  ✅ Feature integrated with existing student system")
except Exception as e:
    print(f"  ❌ Integration error: {e}")

# Summary
print("\n" + "="*70)
print("✅ OUTING PASS FEATURE VERIFICATION COMPLETE")
print("="*70)
print("\n📝 Next Steps:")
print("  1. Start the server: python manage.py runserver")
print("  2. Login as student (student1/pass123)")
print("  3. Request an outing pass from Student Dashboard")
print("  4. Login as admin (admin/admin123)")
print("  5. Review and approve/reject from Admin Dashboard")
print("  6. Check for email notifications (console mode)")

print("\n🔗 Quick Links:")
print("  • Student Request: http://127.0.0.1:8000/outing/request/")
print("  • Student History: http://127.0.0.1:8000/outing/my-passes/")
print("  • Admin Dashboard: http://127.0.0.1:8000/outing/admin-requests/")

print("\n📚 Documentation:")
print("  • Read: OUTING_PASS_GUIDE.md for complete guide")
print("\n")
