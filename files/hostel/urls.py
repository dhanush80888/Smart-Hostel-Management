from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.custom_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('rooms/', views.rooms_list, name='rooms'),
    path('rooms/<int:pk>/', views.room_detail, name='room_detail'),
    path('complaints/new/', views.submit_complaint, name='submit_complaint'),
    path('complaints/', views.complaints_list, name='complaints'),
    path('complaints/<int:pk>/update/', views.update_complaint, name='update_complaint'),
    path('allocate/', views.allocate_room, name='allocate_room'),
    path('mutual-transfer/', views.mutual_transfer, name='mutual_transfer'),
    path('pay/', views.make_payment, name='make_payment'),
    path('outing/request/', views.request_outing_pass, name='request_outing_pass'),
    path('outing/my-passes/', views.my_outing_passes, name='my_outing_passes'),
    path('outing/admin-requests/', views.admin_outing_requests, name='admin_outing_requests'),
    path('outing/approve/<int:pk>/', views.approve_outing_pass, name='approve_outing_pass'),
    path('outing/reject/<int:pk>/', views.reject_outing_pass, name='reject_outing_pass'),
    # Visitor Management URLs
    path('visitor/register/', views.visitor_register, name='visitor_register'),
    path('visitor/status/', views.visitor_status, name='visitor_status'),
    path('visitor/admin-requests/', views.admin_visitor_requests, name='admin_visitor_requests'),
    path('visitor/approve/<int:pk>/', views.approve_visitor, name='approve_visitor'),
    path('visitor/reject/<int:pk>/', views.reject_visitor, name='reject_visitor'),
    path('visitor/log/', views.visitor_log, name='visitor_log'),
    path('visitor/mark-entry/<int:pk>/', views.mark_entry, name='mark_entry'),
    path('visitor/mark-exit/<int:pk>/', views.mark_exit, name='mark_exit'),
    path('security/dashboard/', views.security_dashboard, name='security_dashboard'),
]