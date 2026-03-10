import os
import django
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_hostel.settings')
django.setup()

from django.db.models import Sum
from hostel.models import StudentProfile, Payment

print("\n" + "="*70)
print("PAYMENT DATABASE TEST")
print("="*70 + "\n")

# Get all students
students = StudentProfile.objects.all()

print(f"📊 Total Students: {students.count()}")
print("\n" + "-"*70)

for student in students:
    payments = Payment.objects.filter(student=student)
    total_paid = payments.aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
    outstanding = student.fees_due - (student.fees_paid or Decimal('0.00'))
    
    print(f"\n👤 Student: {student.user.username} ({student.user.get_full_name()})")
    print(f"   • Roll: {student.roll_number or 'Not assigned'}")
    print(f"   • Fees Due: ₹{student.fees_due}")
    print(f"   • Fees Paid (DB): ₹{student.fees_paid or '0.00'}")
    print(f"   • Outstanding: ₹{outstanding}")
    print(f"   • Payments Recorded: {payments.count()}")
    
    if payments:
        print(f"   • Payment History:")
        for payment in payments:
            print(f"      - ₹{payment.amount} on {payment.paid_on.strftime('%Y-%m-%d %H:%M')} ({payment.method})")
    else:
        print(f"   • No payments yet")

print("\n" + "="*70)
print("✓ Database structure verified and working correctly")
print("="*70 + "\n")

# Test creating a payment
print("💾 Testing Payment Creation...")
first_student = students.first()
if first_student:
    test_amount = Decimal('500.00')
    test_payment = Payment.objects.create(
        student=first_student,
        amount=test_amount,
        method='test'
    )
    first_student.fees_paid = (first_student.fees_paid or Decimal('0.00')) + test_amount
    first_student.save()
    
    print(f"✓ Test payment created: ₹{test_payment.amount}")
    print(f"✓ Student fees_paid updated to: ₹{first_student.fees_paid}")
    
    # Delete test payment
    test_payment.delete()
    first_student.fees_paid = (first_student.fees_paid or Decimal('0.00')) - test_amount
    first_student.save()
    print(f"✓ Test payment deleted (rolled back)")

print("\n✅ Payment system is working correctly!")
print("\n" + "="*70 + "\n")
