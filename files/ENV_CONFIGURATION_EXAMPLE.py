"""
Environment-based Email Configuration
Use this for secure credential management (recommended for production)

Steps to use:
1. Create a .env file in project root with:
   EMAIL_HOST_USER=your_email@gmail.com
   EMAIL_HOST_PASSWORD=your_app_password

2. Install python-decouple:
   pip install python-decouple

3. Replace the email settings section in smart_hostel/settings.py with:
   from decouple import config
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='your_email@gmail.com')
   EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='your_app_password')
   DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default=config('EMAIL_HOST_USER'))
"""

# Example .env file (save as .env in project root):
"""
# Smart Hostel Email Configuration
EMAIL_HOST_USER=hostel.notifications@gmail.com
EMAIL_HOST_PASSWORD=abcd efgh ijkl mnop
DEFAULT_FROM_EMAIL=hostel.notifications@gmail.com

# Optional: For other email providers
# SENDGRID_API_KEY=your_sendgrid_key
# MAILGUN_API_KEY=your_mailgun_key
"""

# After creating .env file, add to .gitignore:
"""
.env
*.env
.env.local
.env.*.local
"""
