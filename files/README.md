# Smart Hostel Management System

A Django-based hostel management application for allocating rooms, tracking fees, and managing complaints.

## Features

- **Admin Dashboard** - View total rooms, occupancy, student count, and open complaints
- **Room Management** - Admin can allocate rooms and set rental fees
- **Student Dashboard** - Students can view room assignment, fees, and payment history
- **Fee Tracking** - Track due amounts, payments, and outstanding balances
- **Complaint System** - Students can submit complaints with tracking and admin response
- **Responsive UI** - Built with Bootstrap 5 for mobile-friendly interface

## Project Structure

```
smart_hostel/          # Django project settings
hostel/                # Main application
  - models.py          # Database models (Room, StudentProfile, Payment, Complaint)
  - views.py           # View logic for all pages
  - forms.py           # Registration and complaint forms
  - urls.py            # URL routing
templates/             # HTML templates
  - hostel/            # App templates
  - registration/      # Login template
static/                # CSS, JS files
db.sqlite3             # SQLite database
manage.py              # Django management script
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip

### Windows Setup

1. **Clone/Download the project** and navigate to the folder:
   ```powershell
   cd c:\Users\User\Desktop\files
   ```

2. **Install dependencies** (if requirements.txt exists):
   ```powershell
   pip install django
   ```

3. **Apply database migrations**:
   ```powershell
   python manage.py migrate
   ```

4. **Create admin user and sample data**:
   ```powershell
   python setup_data.py
   ```

5. **Run the development server**:
   ```powershell
   python manage.py runserver
   ```

6. **Access the application**:
   - Home: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/
   - Login: http://127.0.0.1:8000/accounts/login/

## Test Credentials

### Admin Account
- **Username**: admin
- **Password**: admin123

### Student Accounts
- **Username**: student1 | **Password**: pass123
- **Username**: student2 | **Password**: pass123
- **Username**: student3 | **Password**: pass123

## Database Models

### Room
- room_no (unique ID)
- capacity (max students)
- rent (monthly fee)
- is_active (status)

### StudentProfile
- user (OneToOne with User)
- roll_number
- room (ForeignKey to Room)
- fees_due
- fees_paid
- joined_on

### Payment
- student (ForeignKey)
- amount
- paid_on
- method (offline/online)

### Complaint
- student (ForeignKey)
- title
- description
- status (open/in_progress/resolved)
- response
- anonymous (can submit anonymously)
- created_at
- updated_at

## Key Features Explained

### Admin Dashboard
- View total rooms, occupancy statistics
- Count of active students
- Number of open complaints
- List of recent complaints with status

### Student Dashboard
- View assigned room and details
- Track fees due vs. paid
- Outstanding balance calculation
- Recent payment history
- Recent complaints with status

### Room Allocation
- Admin can assign rooms to students
- Fees automatically set from room rent
- View all allocations in table

### Payment System
- Students can record payments
- Fees paid are tracked and updated
- Outstanding amount calculated automatically

### Complaint Management
- Students submit titled complaints with description
- Can submit anonymously
- Admin can view all complaints
- Admin can update complaint status and add responses
- Students can track complaint status

## API/Views

- `home/` - Landing page
- `signup/` - Student registration
- `dashboard/` - Admin or Student dashboard (role-based)
- `rooms/` - List all available rooms
- `rooms/<id>/` - Room details and occupants
- `complaints/` - List complaints
- `complaints/new/` - Submit new complaint
- `allocate/` - Room allocation (Admin only)
- `pay/` - Payment recording
- `accounts/login/` - Login page
- `/admin/` - Django admin interface

## Data Verification

Run the verification script to check all data:
```powershell
python verify_data.py
```

This will display:
- Total users, admins, and students
- Room allocation statistics
- Complaint counts by status
- Payment records
- Test credentials

## Troubleshooting

### Server won't start
- Ensure you're in the correct directory
- Check Python version: `python --version`
- Run migrations: `python manage.py migrate`

### Can't login
- Check that admin/student accounts exist: `python verify_data.py`
- Use test credentials provided above

### Database errors
- Delete `db.sqlite3` and run: `python manage.py migrate` then `python setup_data.py`

### Static files not loading
- Run: `python manage.py collectstatic` (usually not needed in development)

## Notes

- This is a development/demo project using SQLite
- For production, use PostgreSQL or MySQL
- Password validators are disabled for testing
- Email functionality is not implemented
- Payments are simulated (not connected to real gateways)

## Future Enhancements

- Real payment gateway integration (Stripe, PayPal)
- Email notifications for payments and complaint updates
- File uploads for complaint attachments
- Room images and virtual tours
- Automated room allocation algorithm
- Student waiting lists
- Multi-hostel support
- Mobile app (React Native/Flutter)

---

**Version**: 1.0  
**Last Updated**: January 24, 2026  
**Status**: ✓ Fully Functional