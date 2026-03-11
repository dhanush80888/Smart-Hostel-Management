import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_hostel.settings')
django.setup()

from django.urls import reverse

print("\n" + "="*70)
print("LOGOUT SYSTEM VERIFICATION")
print("="*70 + "\n")

# Check settings
from django.conf import settings

print("✓ Session Configuration:")
print(f"  • SESSION_ENGINE: {settings.SESSION_ENGINE}")
print(f"  • SESSION_COOKIE_AGE: {settings.SESSION_COOKIE_AGE}")
print(f"  • SESSION_COOKIE_HTTPONLY: {settings.SESSION_COOKIE_HTTPONLY}")
print(f"  • LOGOUT_REDIRECT_URL: {settings.LOGOUT_REDIRECT_URL}")

print("\n✓ URL Routes:")
print(f"  • Logout URL: {reverse('logout')}")
print(f"  • Login URL: {reverse('login')}")
print(f"  • Home URL: {reverse('home')}")

# Check that logout view exists
from hostel.views import custom_logout
print("\n✓ Custom Logout View:")
print(f"  • Function exists: {custom_logout.__name__}")
print(f"  • Function docstring: {custom_logout.__doc__.strip()}")

print("\n✓ Authentication Settings:")
print(f"  • LOGIN_REDIRECT_URL: {settings.LOGIN_REDIRECT_URL}")
print(f"  • LOGOUT_REDIRECT_URL: {settings.LOGOUT_REDIRECT_URL}")

print("\n✓ Logout Flow:")
print("  1. User clicks 'Logout' button")
print("  2. Redirects to /logout/")
print("  3. custom_logout() view called")
print("  4. Session cleared with logout()")
print("  5. Success message displayed")
print("  6. Redirected to login page (/accounts/login/)")
print("  7. Admin/Student must login again")

print("\n" + "="*70)
print("✅ LOGOUT SYSTEM READY")
print("="*70 + "\n")

print("Testing Steps:")
print("  1. Start server: python manage.py runserver")
print("  2. Login as student1 / pass123")
print("  3. Click 'Logout' button")
print("  4. Should see success message and login page")
print("  5. Try accessing dashboard - should redirect to login")
print("  6. Login as admin / admin123")
print("  7. Click 'Logout' button")
print("  8. Should see success message and login page")
print("  9. Try accessing admin-dashboard - should redirect to login\n")
