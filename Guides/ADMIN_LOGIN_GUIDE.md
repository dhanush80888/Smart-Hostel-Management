# 🔐 HOW TO LOGIN AS ADMIN

## Admin Credentials

```
Username: admin
Password: admin123
```

---

## Step-by-Step: Login as Admin

### Step 1: Start the Server
```powershell
cd c:\Users\User\Desktop\files
python manage.py runserver
```

✅ You should see:
```
Starting development server at http://127.0.0.1:8000/
```

### Step 2: Open Browser
Go to: **http://127.0.0.1:8000/accounts/login/**

You will see the login page:
```
┌─────────────────────────────┐
│          Login              │
├─────────────────────────────┤
│ Username: [_____________]   │
│ Password: [_____________]   │
│          [LOGIN BUTTON]     │
└─────────────────────────────┘
```

### Step 3: Enter Admin Credentials
- **Username field**: Type `admin`
- **Password field**: Type `admin123`

### Step 4: Click LOGIN Button
Click the blue [LOGIN] button

### Step 5: Admin Dashboard Opens
✅ You will see the **Admin Dashboard** with:
- Total Rooms: 5
- Occupied Rooms: 3
- Total Students: 5
- Open Complaints: 2
- Total Revenue Collected: ₹5000
- Recent Complaints list
- Quick Action buttons

---

## Admin Dashboard Features

Once logged in as admin, you can:

### 1. **View Statistics**
   - Total rooms count
   - Occupancy status
   - Student count
   - Open complaints count
   - Revenue collected

### 2. **Allocate Rooms**
   - Click "Allocate Rooms" button
   - Assign rooms to students
   - Set room rent

### 3. **View Complaints**
   - See all student complaints
   - View complaint status
   - Respond to complaints

### 4. **Access Django Admin**
   - Click "Django Admin"
   - Full database management

---

## Admin Dashboard URL
Direct link: **http://127.0.0.1:8000/admin-dashboard/**

---

## What Admin Can Do

### Room Management
- View all rooms (5 rooms available)
- Room occupancy details
- Allocate rooms to students
- Check room capacity

### Student Management
- View all students (5 students)
- See room assignments
- Track fees and payments

### Complaint Management
- View all complaints (3 complaints)
- See complaint status:
  - Open
  - In Progress
  - Resolved
- Add responses to complaints

### Revenue Tracking
- Total revenue collected: ₹5000
- Payment records
- Student fee status

### Quick Actions
```
[View Rooms]  [Allocate Rooms]  [View Complaints]  [Django Admin]
```

---

## Admin vs Student Dashboard

### Admin Sees:
- 📊 Statistics (rooms, students, complaints, revenue)
- 💼 Management tools (allocate, manage)
- 📈 Analytics (occupancy, revenue)
- 🔧 Admin panel access

### Student Sees:
- 👤 Personal profile
- 💰 Fee information
- 💳 Payment history
- 📝 Complaint tracking

---

## Example Admin Session

```
1. Login with: admin / admin123
   ↓
2. See Admin Dashboard
   ↓
3. View Statistics:
   • Rooms: 5
   • Occupied: 3
   • Students: 5
   • Complaints: 2
   • Revenue: ₹5000
   ↓
4. Click "Allocate Rooms"
   ↓
5. Assign room to student
   ↓
6. See updated statistics
   ↓
7. Click "View Complaints"
   ↓
8. See complaint list
   ↓
9. Click "Django Admin"
   ↓
10. Full database access
```

---

## Useful URLs for Admin

```
Admin Dashboard:        http://127.0.0.1:8000/admin-dashboard/
Allocate Rooms:        http://127.0.0.1:8000/allocate/
View Complaints:       http://127.0.0.1:8000/complaints/
Django Admin Panel:    http://127.0.0.1:8000/admin/
Home Page:             http://127.0.0.1:8000/
Logout:                http://127.0.0.1:8000/logout/
```

---

## Admin Login Tips

### ✅ DO:
- Use exact credentials: `admin` / `admin123`
- Make sure server is running
- Clear browser cache if having issues
- Use incognito window if stuck

### ❌ DON'T:
- Don't modify admin password (unless you need to)
- Don't close the server while using
- Don't use wrong credentials

---

## Troubleshooting

### "Login failed" Error
- Check username: `admin` (lowercase)
- Check password: `admin123` (exact)
- Ensure server is running

### Can't access admin-dashboard
- Make sure you're logged in as admin
- Try logging out and logging in again
- Clear browser cookies

### Server not running
```powershell
# Make sure you're in the right directory
cd c:\Users\User\Desktop\files

# Start server
python manage.py runserver
```

---

## Security Note

⚠️ **Important**:
- This admin account is for development/testing
- For production, change the password
- Never share admin credentials
- Use strong passwords in production

---

## Quick Reference Card

```
┌────────────────────────────────┐
│     ADMIN LOGIN CARD           │
├────────────────────────────────┤
│ URL: /accounts/login/          │
│ Username: admin                │
│ Password: admin123             │
│ Dashboard: /admin-dashboard/   │
│ Status: ✅ Ready               │
└────────────────────────────────┘
```

---

## Next Steps

1. **Start Server**
   ```powershell
   python manage.py runserver
   ```

2. **Go to Login Page**
   ```
   http://127.0.0.1:8000/accounts/login/
   ```

3. **Enter Credentials**
   ```
   Username: admin
   Password: admin123
   ```

4. **Click LOGIN**
   ```
   ✅ Admin Dashboard loads
   ```

5. **Explore Admin Features**
   ```
   • View Statistics
   • Allocate Rooms
   • View Complaints
   • Django Admin
   ```

---

**Ready to login as admin?** Start your server now! 🚀
