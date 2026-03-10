from django.contrib import admin
from .models import (
    Room, StudentProfile, Payment, Complaint,
    WeeklyMenu, MealAttendance, FoodFeedback, MessMenu,
    Announcement, MaintenanceRequest, EmergencyAlert,
    LeaveRequest, LostItem, StudentID, ElectricityUsage,
    ChatMessage,
)

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


@admin.register(WeeklyMenu)
class WeeklyMenuAdmin(admin.ModelAdmin):
    list_display = ('day', 'is_active')
    list_editable = ('is_active',)
    ordering = ('day',)


@admin.register(MealAttendance)
class MealAttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'meal_type', 'status')
    list_filter = ('meal_type', 'status', 'date')
    search_fields = ('student__user__username','student__user__first_name','student__user__last_name')


@admin.register(FoodFeedback)
class FoodFeedbackAdmin(admin.ModelAdmin):
    list_display = ('student', 'meal_type', 'rating', 'date')
    list_filter = ('meal_type', 'rating', 'date')
    search_fields = ('student__user__username','student__user__first_name','student__user__last_name')


@admin.register(MessMenu)
class MessMenuAdmin(admin.ModelAdmin):
    list_display = ('date', 'meal_type', 'is_active')
    list_filter = ('meal_type', 'date')
    ordering = ('-date',)

# new model registrations
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_by', 'created_at', 'expiry_date', 'is_important')
    list_filter = ('category', 'is_important')
    search_fields = ('title', 'message')

@admin.register(MaintenanceRequest)
class MaintenanceRequestAdmin(admin.ModelAdmin):
    list_display = ('student', 'room_number', 'issue_type', 'status', 'assigned_staff', 'created_at')
    list_filter = ('issue_type', 'status')
    search_fields = ('room_number', 'description', 'student__user__username')

@admin.register(EmergencyAlert)
class EmergencyAlertAdmin(admin.ModelAdmin):
    list_display = ('student', 'room_number', 'alert_type', 'status', 'created_at')
    list_filter = ('alert_type', 'status')
    readonly_fields = ('student','room_number','alert_type','message','created_at')

@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('student', 'start_date', 'end_date', 'status', 'parent_approval', 'warden_approval')
    list_filter = ('status', 'parent_approval', 'warden_approval')
    search_fields = ('student__user__username',)

@admin.register(LostItem)
class LostItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'status', 'reported_by', 'created_at')
    list_filter = ('status',)
    search_fields = ('item_name', 'location')

@admin.register(StudentID)
class StudentIDAdmin(admin.ModelAdmin):
    list_display = ('student', 'issued_date')

@admin.register(ElectricityUsage)
class ElectricityUsageAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'month', 'units_consumed')
    list_filter = ('month',)
    search_fields = ('room_number',)

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at', 'is_from_user')
    list_filter = ('is_from_user', 'created_at')
    search_fields = ('user__username', 'message')
    readonly_fields = ('user', 'message', 'response', 'created_at')
