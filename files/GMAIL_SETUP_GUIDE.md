# Gmail Email Notification Setup Guide

This guide will help you configure real Gmail SMTP to send email notifications when outing pass requests are approved or rejected.

## Step 1: Enable 2-Factor Authentication on Gmail

1. Go to https://myaccount.google.com/
2. Click on "Security" in the left menu
3. Scroll to "How you sign in to Google"
4. Click on "2-Step Verification"
5. Follow the steps to enable 2-Factor Authentication
6. You'll need a phone number and authenticator app or SMS codes

## Step 2: Generate Gmail App Password

1. Go to https://myaccount.google.com/apppasswords
2. You'll see a prompt to select your app and device
3. Select:
   - **App**: Mail
   - **Device**: Windows Computer (or your OS)
4. Click "Generate"
5. Google will display a 16-character app password (it looks like: `xxxx xxxx xxxx xxxx`)
6. **Copy this password** - you'll need it next

## Step 3: Configure Django Settings

Edit `smart_hostel/settings.py` and update the Gmail configuration:

```python
EMAIL_HOST_USER = 'your_email@gmail.com'  # Your Gmail address
EMAIL_HOST_PASSWORD = 'your_app_password'  # The 16-character password from Step 2
DEFAULT_FROM_EMAIL = 'your_email@gmail.com'  # Same as EMAIL_HOST_USER
```

### Example:
```python
EMAIL_HOST_USER = 'hostel.manager@gmail.com'
EMAIL_HOST_PASSWORD = 'abcd efgh ijkl mnop'  # 16-character app password
DEFAULT_FROM_EMAIL = 'hostel.manager@gmail.com'
```

## Step 4: Update Database (Guardian Emails)

When students request an outing pass, they provide their guardian's email. Make sure these emails are correct.

## Step 5: Test the Configuration

Use the test script to verify everything works:

```bash
python test_email_notification.py
```

This will attempt to send a test email to verify the configuration.

## Step 6: Use the Feature

1. Student logs in and requests an outing pass
2. Provides guardian's email address
3. Admin reviews the request
4. Admin clicks "Approve" or "Reject"
5. **Real email sent to guardian's inbox** ✅

## Troubleshooting

### Issue: "Login failed for user"
- Verify you're using an **App Password**, not your regular Gmail password
- App passwords are only available if 2-Factor Authentication is enabled
- Generate a new app password at https://myaccount.google.com/apppasswords

### Issue: "Connection timeout"
- Check your internet connection
- Verify port 587 is not blocked by firewall
- Try port 465 (SSL) as alternative:
  ```python
  EMAIL_PORT = 465
  EMAIL_USE_TLS = False
  EMAIL_USE_SSL = True
  ```

### Issue: "Emails not arriving"
- Check Gmail spam folder
- Verify guardian email addresses are correct
- Check Django logs for errors: `python manage.py shell`

### Issue: "SMTP Error: 534"
- Your app password might be incorrect
- Regenerate a new app password
- Ensure you copied all 16 characters including spaces

### Issue: Less Secure App Access
If you have an older Gmail account without 2FA, enable "Less secure app access":
1. Go to https://myaccount.google.com/security
2. Scroll to "Less secure app access"
3. Turn it ON
4. Use your regular Gmail password (not recommended for production)

## Security Best Practices

1. **Never commit credentials** to version control
2. **Use environment variables** for production (recommended):
   ```python
   import os
   EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
   EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
   ```

3. **Use App Passwords**, not your main Gmail password
4. **For Production**: Use a dedicated Gmail account for notifications
5. **Monitor**: Check Gmail security activity regularly

## Alternative Email Providers

If you don't want to use Gmail, you can use:

- **SendGrid** (free tier available):
  ```python
  EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
  SENDGRID_API_KEY = 'your_api_key'
  ```

- **AWS SES** (pay-per-use)
- **MailGun** (free tier for development)

## Environment Variable Setup (Recommended for Production)

1. Create a `.env` file in project root:
   ```
   EMAIL_HOST_USER=your_email@gmail.com
   EMAIL_HOST_PASSWORD=xxxx xxxx xxxx xxxx
   ```

2. Install python-decouple:
   ```bash
   pip install python-decouple
   ```

3. Update settings.py:
   ```python
   from decouple import config
   EMAIL_HOST_USER = config('EMAIL_HOST_USER')
   EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
   ```

4. Add `.env` to `.gitignore`:
   ```
   .env
   *.env
   ```

## Email Template Customization

The email templates are in `hostel/views.py` in the `send_guardian_notification()` function.

You can customize:
- Subject line
- Email body/message
- Sender name
- HTML formatting (can be enhanced with HTML emails)

## Monitoring Sent Emails

Django by default logs emails. Check if emails were sent:
```bash
python manage.py shell
```

```python
# Check if notification was marked as sent
from hostel.models import OutingPass
outing = OutingPass.objects.first()
print(f"Notification sent: {outing.notification_sent}")
```

## Support

For Gmail issues: https://support.google.com/mail/
For Django email issues: https://docs.djangoproject.com/en/5.2/topics/email/
