from django.contrib import admin
from .models import Room, StudentProfile, Payment, Complaint

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_no', 'capacity', 'rent', 'is_active')

@admin.register(StudentProfile)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'roll_number', 'room', 'fees_due', 'fees_paid')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('student', 'amount', 'paid_on', 'method')

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('title', 'student', 'status', 'created_at')
    list_filter = ('status',)