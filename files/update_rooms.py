import os
import django
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_hostel.settings')
django.setup()

from hostel.models import Room

# Update all existing rooms to have capacity 4 and rent 5000
rooms = Room.objects.all()
updated_count = 0

for room in rooms:
    if room.capacity != 4 or room.rent != Decimal('5000.00'):
        room.capacity = 4
        room.rent = Decimal('5000.00')
        room.save()
        updated_count += 1
        print(f"✓ Updated Room {room.room_no}: capacity=4, rent=₹5000")

print(f"\n✓ Updated {updated_count} room(s) with new specifications")
print("✓ All rooms now have capacity of 4 persons and rent of ₹5000")