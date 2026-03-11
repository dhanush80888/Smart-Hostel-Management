from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Count, Sum, F
from decimal import Decimal
import random
from .forms import StudentSignUpForm, ComplaintForm, ComplaintUpdateForm, AllocateRoomForm, MutualTransferForm, OutingPassForm
from .models import StudentProfile, Room, Complaint, Payment, OutingPass, Announcement, MessMenu, Visitor, VisitorLog
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'hostel/home.html')

def signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()
            # update profile fields
            try:
                profile = user.studentprofile
            except StudentProfile.DoesNotExist:
                profile = StudentProfile.objects.create(user=user)
            roll = form.cleaned_data.get('roll_number')
            fees_due = form.cleaned_data.get('fees_due') or 0
            if roll:
                profile.roll_number = roll
            profile.fees_due = fees_due
            profile.save()
            login(request, user)
            messages.success(request, 'Account created. Welcome!')
            return redirect('dashboard')
        else:
            # form is invalid, pass it back to show errors
            pass
    else:
        form = StudentSignUpForm()
    return render(request, 'hostel/signup.html', {'form': form})

@login_required
def dashboard(request):
    # Redirect admins to admin dashboard, students to student dashboard
    if request.user.is_staff:
        return redirect('admin_dashboard')
    return redirect('student_dashboard')

@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('student_dashboard')
    
    # Admin dashboard: summary
    total_rooms = Room.objects.count()
    occupied = Room.objects.annotate(o=Count('studentprofile')).filter(o__gt=0).count()
    total_students = StudentProfile.objects.count()
    complaints_open = Complaint.objects.filter(status='open').count()
    recent_complaints = Complaint.objects.order_by('-created_at')[:6]
    total_revenue = Payment.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    
    # Visitor statistics
    pending_visitors = Visitor.objects.filter(status='pending').count()
    approved_visitors_today = Visitor.objects.filter(status='approved', visiting_date=timezone.now().date()).count()
    total_visitors_today = Visitor.objects.filter(visiting_date=timezone.now().date()).count()
    
    context = {
        'total_rooms': total_rooms,
        'occupied': occupied,
        'total_students': total_students,
        'complaints_open': complaints_open,
        'recent_complaints': recent_complaints,
        'total_revenue': total_revenue,
        'pending_visitors': pending_visitors,
        'approved_visitors_today': approved_visitors_today,
        'total_visitors_today': total_visitors_today,
    }
    return render(request, 'hostel/admin_dashboard.html', context)

@login_required
def student_dashboard(request):
    # Redirect staff to admin dashboard
    if request.user.is_staff:
        return redirect('admin_dashboard')
    
    try:
        profile = request.user.studentprofile
    except StudentProfile.DoesNotExist:
        messages.error(request, 'Your student profile is not set up. Please contact admin.')
        return redirect('logout')

    payments = Payment.objects.filter(student=profile).order_by('-paid_on')[:5]
    complaints = Complaint.objects.filter(student=profile).order_by('-created_at')[:5]
    leave_requests = OutingPass.objects.filter(student=profile).order_by('-requested_on')[:5]
    announcements = Announcement.objects.filter(is_active=True).order_by('-created_at')[:3]

    # Get counts
    total_complaints = Complaint.objects.filter(student=profile).count()
    total_payments = Payment.objects.filter(student=profile).count()

    # Get today's mess menu
    from datetime import date
    today = date.today()
    todays_menu = MessMenu.objects.filter(date=today, is_active=True)

    context = {
        'profile': profile,
        'payments': payments,
        'complaints': complaints,
        'leave_requests': leave_requests,
        'announcements': announcements,
        'todays_menu': todays_menu,
        'total_complaints': total_complaints,
        'total_payments': total_payments,
    }
    return render(request, 'hostel/student_dashboard.html', context)

@login_required
def rooms_list(request):
    rooms = Room.objects.filter(is_active=True).order_by('room_no')
    for room in rooms:
        room.availability_percentage = int((room.occupants_count / room.capacity * 100) if room.capacity > 0 else 0)
        room.spots_available = room.capacity - room.occupants_count
    return render(request, 'hostel/rooms.html', {'rooms': rooms})

@login_required
def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    occupants = room.studentprofile_set.all()
    return render(request, 'hostel/room_detail.html', {'room': room, 'occupants': occupants})

@login_required
def submit_complaint(request):
    # Redirect staff users to admin dashboard
    if request.user.is_staff:
        return redirect('admin_dashboard')
    
    # Check if user has a student profile
    try:
        profile = request.user.studentprofile
    except StudentProfile.DoesNotExist:
        messages.error(request, 'Your student profile is not set up. Please contact admin.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.student = profile
            if c.anonymous:
                # optional: clear identifying info in title/desc? we keep student link but display anonymous flag
                pass
            c.save()
            messages.success(request, 'Complaint submitted.')
            return redirect('dashboard')
    else:
        form = ComplaintForm()
    return render(request, 'hostel/submit_complaint.html', {'form': form})

@login_required
def complaints_list(request):
    if request.user.is_staff:
        complaints = Complaint.objects.order_by('-created_at')
    else:
        profile = request.user.studentprofile
        complaints = Complaint.objects.filter(student=profile).order_by('-created_at')
    return render(request, 'hostel/complaints_list.html', {'complaints': complaints})

@user_passes_test(lambda u: u.is_staff)
def update_complaint(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)
    if request.method == 'POST':
        form = ComplaintUpdateForm(request.POST, instance=complaint)
        if form.is_valid():
            form.save()
            messages.success(request, 'Complaint updated successfully.')
            return redirect('complaints')
    else:
        form = ComplaintUpdateForm(instance=complaint)
    return render(request, 'hostel/update_complaint.html', {'form': form, 'complaint': complaint})

@user_passes_test(lambda u: u.is_staff)
def allocate_room(request):
    if request.method == 'POST':
        form = AllocateRoomForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                user = User.objects.get(username=username)
                profile = user.studentprofile
                # Get available rooms
                available_rooms = Room.objects.filter(is_active=True).annotate(occupants=Count('studentprofile')).filter(occupants__lt=F('capacity'))
                if not available_rooms:
                    messages.error(request, 'No available rooms.')
                else:
                    # Randomly select a room
                    room = random.choice(list(available_rooms))
                    profile.room = room
                    # optional: set fees due as room rent if 0
                    if profile.fees_due in (None, 0):
                        profile.fees_due = room.rent
                    profile.save()
                    messages.success(request, f'Room {room.room_no} allocated randomly to {user.username}.')
            except User.DoesNotExist:
                messages.error(request, 'User not found.')
            return redirect('allocate_room')
    else:
        form = AllocateRoomForm()
    students = StudentProfile.objects.select_related('user','room')
    rooms = Room.objects.filter(is_active=True)
    return render(request, 'hostel/allocate_room.html', {'form': form, 'students': students, 'rooms': rooms})

@user_passes_test(lambda u: u.is_staff)
def mutual_transfer(request):
    if request.method == 'POST':
        form = MutualTransferForm(request.POST)
        if form.is_valid():
            student1 = form.cleaned_data['student1']
            student2 = form.cleaned_data['student2']
            
            if student1 == student2:
                messages.error(request, 'Please select two different students.')
                return redirect('mutual_transfer')
            
            # Swap rooms
            room1 = student1.room
            room2 = student2.room
            
            student1.room = room2
            student2.room = room1
            
            student1.save()
            student2.save()
            
            messages.success(request, f'Rooms swapped successfully! {student1.user.username} now in {room2.room_no} and {student2.user.username} now in {room1.room_no}.')
            return redirect('mutual_transfer')
    else:
        form = MutualTransferForm()
    
    # Get students with rooms for display
    students_with_rooms = StudentProfile.objects.filter(room__isnull=False).select_related('user', 'room')
    return render(request, 'hostel/mutual_transfer.html', {'form': form, 'students': students_with_rooms})

@login_required
def make_payment(request):
    if request.user.is_staff:
        return redirect('admin_dashboard')
    profile = request.user.studentprofile
    if request.method == 'POST':
        amount = request.POST.get('amount')
        method = request.POST.get('method', 'online')
        try:
            amt = Decimal(amount)
            if amt <= 0:
                raise ValueError
        except Exception as e:
            messages.error(request, 'Enter a valid amount.')
            return redirect('make_payment')
        
        # Create payment record
        payment = Payment.objects.create(student=profile, amount=amt, method=method)
        
        # Update fees_paid
        profile.fees_paid = (profile.fees_paid or Decimal('0.00')) + amt
        profile.save()
        
        messages.success(request, f'Payment of ₹{amt} recorded successfully! (Method: {method})')
        return redirect('student_dashboard')
    
    # Calculate outstanding
    outstanding = profile.fees_due - (profile.fees_paid or Decimal('0.00'))
    
    # Get recent payments for display
    payments = Payment.objects.filter(student=profile).order_by('-paid_on')[:10]
    
    return render(request, 'hostel/make_payment.html', {'profile': profile, 'outstanding': outstanding, 'payments': payments})

def custom_logout(request):
    """Custom logout view that clears session and redirects to login"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

@login_required
def request_outing_pass(request):
    """Student requests an outing pass"""
    if request.user.is_staff:
        return redirect('admin_dashboard')
    profile = request.user.studentprofile
    
    if request.method == 'POST':
        form = OutingPassForm(request.POST)
        if form.is_valid():
            outing = form.save(commit=False)
            outing.student = profile
            outing.save()
            messages.success(request, 'Outing pass request submitted! Waiting for admin approval.')
            return redirect('my_outing_passes')
    else:
        form = OutingPassForm()
    
    return render(request, 'hostel/request_outing_pass.html', {'form': form})

@login_required
def my_outing_passes(request):
    """Student views their outing passes"""
    if request.user.is_staff:
        return redirect('admin_dashboard')
    profile = request.user.studentprofile
    passes = OutingPass.objects.filter(student=profile).order_by('-requested_on')
    
    return render(request, 'hostel/my_outing_passes.html', {'passes': passes})

@login_required
def admin_outing_requests(request):
    """Admin views all outing pass requests"""
    if not request.user.is_staff:
        messages.error(request, 'Unauthorized access.')
        return redirect('dashboard')
    
    pending = OutingPass.objects.filter(status='pending').order_by('requested_on')
    approved = OutingPass.objects.filter(status='approved').order_by('-approved_on')
    rejected = OutingPass.objects.filter(status='rejected').order_by('-requested_on')
    
    return render(request, 'hostel/admin_outing_requests.html', {
        'pending': pending,
        'approved': approved,
        'rejected': rejected
    })

@login_required
def approve_outing_pass(request, pk):
    """Admin approves an outing pass"""
    if not request.user.is_staff:
        messages.error(request, 'Unauthorized access.')
        return redirect('dashboard')
    
    outing = get_object_or_404(OutingPass, pk=pk)
    
    if request.method == 'POST':
        outing.status = 'approved'
        outing.approved_on = timezone.now()
        outing.approved_by = request.user
        outing.save()
        
        # Send notification to guardian
        send_guardian_notification(outing, 'approved')
        
        messages.success(request, f'Outing pass approved for {outing.student.user.get_full_name()}')
        return redirect('admin_outing_requests')
    
    return render(request, 'hostel/approve_outing_pass.html', {'outing': outing})

@login_required
def reject_outing_pass(request, pk):
    """Admin rejects an outing pass"""
    if not request.user.is_staff:
        messages.error(request, 'Unauthorized access.')
        return redirect('dashboard')
    
    outing = get_object_or_404(OutingPass, pk=pk)
    
    if request.method == 'POST':
        rejection_reason = request.POST.get('rejection_reason', '')
        outing.status = 'rejected'
        outing.rejection_reason = rejection_reason
        outing.save()
        
        # Send notification to guardian
        send_guardian_notification(outing, 'rejected')
        
        messages.success(request, f'Outing pass rejected for {outing.student.user.get_full_name()}')
        return redirect('admin_outing_requests')
    
    return render(request, 'hostel/reject_outing_pass.html', {'outing': outing})

def send_guardian_notification(outing, status):
    """Send notification to guardian/parent"""
    try:
        from django.core.mail import send_mail
        from django.conf import settings
        
        student_name = outing.student.user.get_full_name()
        
        if status == 'approved':
            subject = f"Outing Pass Approved - {student_name}"
            message = f"""
Dear Guardian/Parent,

We are pleased to inform you that your ward {student_name} 
has been granted permission for an outing pass.

Details:
- From Date: {outing.from_date.strftime('%d-%m-%Y')}
- To Date: {outing.to_date.strftime('%d-%m-%Y')}
- Duration: {outing.days_requested} day(s)
- Reason: {outing.reason}
- Approved On: {outing.approved_on.strftime('%d-%m-%Y %I:%M %p') if outing.approved_on else 'N/A'}
- Approved By: {outing.approved_by.get_full_name() if outing.approved_by else 'Admin'}

Your ward is permitted to leave the hostel during the specified period.
Please ensure they follow all hostel rules and maintain safety.

Best Regards,
Smart Hostel Management System
"""
        else:  # rejected
            subject = f"Outing Pass Request - Status Update for {student_name}"
            message = f"""
Dear Guardian/Parent,

We regret to inform you that your ward {student_name}'s 
outing pass request has been declined.

Request Details:
- From Date: {outing.from_date.strftime('%d-%m-%Y')}
- To Date: {outing.to_date.strftime('%d-%m-%Y')}
- Duration: {outing.days_requested} day(s)
- Reason: {outing.reason}

Reason for Rejection:
{outing.rejection_reason or 'Not specified'}

If you have any concerns or would like to discuss further, please contact the hostel administration.

Best Regards,
Smart Hostel Management System
"""
        
        recipient_email = outing.guardian_email
        if recipient_email:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL or 'noreply@smarthostel.com',
                [recipient_email],
                fail_silently=False,
            )
            outing.notification_sent = True
            outing.save()
            print(f"\n✅ NOTIFICATION SENT to {recipient_email}\nStatus: {status.upper()}\n")
    except Exception as e:
        print(f"\n❌ Error sending notification: {e}\n")

# Visitor Management Views

@login_required
def visitor_register(request):
    """Student registers a visitor"""
    if request.user.is_staff:
        return redirect('admin_dashboard')
    profile = request.user.studentprofile
    
    if request.method == 'POST':
        visitor_name = request.POST.get('visitor_name')
        phone_number = request.POST.get('phone_number')
        purpose = request.POST.get('purpose')
        visiting_date = request.POST.get('visiting_date')
        expected_entry_time = request.POST.get('expected_entry_time')
        expected_exit_time = request.POST.get('expected_exit_time')
        
        try:
            Visitor.objects.create(
                student=profile,
                visitor_name=visitor_name,
                phone_number=phone_number,
                purpose=purpose,
                visiting_date=visiting_date,
                expected_entry_time=expected_entry_time,
                expected_exit_time=expected_exit_time,
                status='pending'
            )
            messages.success(request, 'Visitor registration submitted successfully! Waiting for approval.')
            return redirect('visitor_status')
        except Exception as e:
            messages.error(request, f'Error registering visitor: {str(e)}')
    
    return render(request, 'hostel/visitor_register.html')

@login_required
def visitor_status(request):
    """Student views visitor request status and history"""
    if request.user.is_staff:
        return redirect('admin_dashboard')
    profile = request.user.studentprofile
    
    visitors = Visitor.objects.filter(student=profile).order_by('-created_at')
    
    return render(request, 'hostel/visitor_status.html', {'visitors': visitors})

@login_required
def admin_visitor_requests(request):
    """Admin views visitor requests"""
    if not request.user.is_staff:
        messages.error(request, 'Unauthorized access.')
        return redirect('dashboard')
    
    pending = Visitor.objects.filter(status='pending').order_by('created_at')
    approved = Visitor.objects.filter(status='approved').order_by('-created_at')
    rejected = Visitor.objects.filter(status='rejected').order_by('-created_at')
    
    return render(request, 'hostel/admin_visitor_requests.html', {
        'pending': pending,
        'approved': approved,
        'rejected': rejected
    })

@login_required
def approve_visitor(request, pk):
    """Admin approves a visitor request"""
    if not request.user.is_staff:
        messages.error(request, 'Unauthorized access.')
        return redirect('dashboard')
    
    visitor = get_object_or_404(Visitor, pk=pk)
    
    if request.method == 'POST':
        visitor.status = 'approved'
        visitor.save()
        
        # Create visitor log
        VisitorLog.objects.create(visitor=visitor)
        
        messages.success(request, f'Visitor {visitor.visitor_name} approved.')
        return redirect('admin_visitor_requests')
    
    return render(request, 'hostel/approve_visitor.html', {'visitor': visitor})

@login_required
def reject_visitor(request, pk):
    """Admin rejects a visitor request"""
    if not request.user.is_staff:
        messages.error(request, 'Unauthorized access.')
        return redirect('dashboard')
    
    visitor = get_object_or_404(Visitor, pk=pk)
    
    if request.method == 'POST':
        visitor.status = 'rejected'
        visitor.save()
        
        messages.success(request, f'Visitor {visitor.visitor_name} rejected.')
        return redirect('admin_visitor_requests')
    
    return render(request, 'hostel/reject_visitor.html', {'visitor': visitor})

@login_required
def visitor_log(request):
    """Security staff views visitor logs and manages entry/exit"""
    if not request.user.is_staff:
        messages.error(request, 'Unauthorized access.')
        return redirect('dashboard')
    
    # Get today's visitors
    today = timezone.now().date()
    visitors_today = Visitor.objects.filter(
        status='approved',
        visiting_date=today
    ).select_related('student')
    
    # Get logs with entry/exit times
    logs = VisitorLog.objects.filter(
        visitor__visiting_date=today
    ).select_related('visitor', 'visitor__student')
    
    return render(request, 'hostel/visitor_log.html', {
        'visitors_today': visitors_today,
        'logs': logs
    })

@login_required
def mark_entry(request, pk):
    """Security marks visitor entry"""
    if not request.user.is_staff:
        messages.error(request, 'Unauthorized access.')
        return redirect('dashboard')
    
    visitor = get_object_or_404(Visitor, pk=pk)
    log, created = VisitorLog.objects.get_or_create(visitor=visitor)
    
    if not log.entry_time:
        log.entry_time = timezone.now()
        log.security_staff = request.user
        log.save()
        messages.success(request, f'Entry time recorded for {visitor.visitor_name}')
    else:
        messages.warning(request, 'Entry time already recorded')
    
    return redirect('visitor_log')

@login_required
def mark_exit(request, pk):
    """Security marks visitor exit"""
    if not request.user.is_staff:
        messages.error(request, 'Unauthorized access.')
        return redirect('dashboard')
    
    visitor = get_object_or_404(Visitor, pk=pk)
    log = get_object_or_404(VisitorLog, visitor=visitor)
    
    if not log.exit_time:
        log.exit_time = timezone.now()
        log.save()
        messages.success(request, f'Exit time recorded for {visitor.visitor_name}')
    else:
        messages.warning(request, 'Exit time already recorded')
    
    return redirect('visitor_log')

@login_required
def security_dashboard(request):
    """Security dashboard with visitor statistics"""
    if not request.user.is_staff:
        messages.error(request, 'Unauthorized access.')
        return redirect('dashboard')
    
    today = timezone.now().date()
    
    # Statistics
    total_visitors_today = Visitor.objects.filter(visiting_date=today).count()
    pending_approvals = Visitor.objects.filter(status='pending').count()
    approved_visitors = Visitor.objects.filter(status='approved', visiting_date=today).count()
    
    # Recent logs
    recent_logs = VisitorLog.objects.filter(
        visitor__visiting_date=today
    ).select_related('visitor', 'visitor__student').order_by('-entry_time')[:10]
    
    return render(request, 'hostel/security_dashboard.html', {
        'total_visitors_today': total_visitors_today,
        'pending_approvals': pending_approvals,
        'approved_visitors': approved_visitors,
        'recent_logs': recent_logs
    })

