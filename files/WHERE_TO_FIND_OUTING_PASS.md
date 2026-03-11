# 🚪 WHERE TO FIND OUTING PASS FEATURE IN THE UI

## 📍 STUDENT DASHBOARD

When you login as a student and go to the Student Dashboard, you'll find:

### Location in UI
```
Student Dashboard
│
├── Profile Section
│   └── Your Name, Roll Number, Room, Fees Info
│
├── Fees Section
│   └── Outstanding Balance, Payment History
│
├── Quick Actions (NEW!)
│   ├── 🚪 REQUEST OUTING PASS ← NEW BUTTON
│   ├── Pay Fees
│   ├── Submit Complaint
│   └── View Complaints
│
└── Other Links
    └── Logout
```

### How to Access
**Path 1**: Direct URL
```
http://127.0.0.1:8000/student-dashboard/
```

**Path 2**: From Dashboard
```
1. Login at: http://127.0.0.1:8000/accounts/login/
2. Username: student1
3. Password: pass123
4. Automatically redirects to Student Dashboard
```

**Path 3**: Direct to Request Form
```
http://127.0.0.1:8000/outing/request/
```

---

## 📋 REQUEST OUTING PASS PAGE

### What You'll See
```
┌─────────────────────────────────────────────────┐
│         📋 Request Outing Pass                  │
├─────────────────────────────────────────────────┤
│                                                 │
│  From Date:        [📅 Calendar Input]          │
│  To Date:          [📅 Calendar Input]          │
│  Number of Days:   [123 Input]                  │
│  Reason:           [Text Area - 4 rows]         │
│  Guardian Email:   [Email Input] *              │
│  Guardian Phone:   [Phone Input]                │
│                                                 │
│  ℹ️ Important: Your request will be reviewed... │
│                                                 │
│  [Submit Request]  [Cancel]                     │
│                                                 │
└─────────────────────────────────────────────────┘
```

### Fields to Fill
1. **From Date**: Click calendar, select start date
2. **To Date**: Click calendar, select end date  
3. **Number of Days**: Type number (e.g., 3)
4. **Reason**: Type your reason (e.g., "Family function")
5. **Guardian Email**: Type parent's email
6. **Guardian Phone**: Type parent's phone (optional)
7. Click **Submit Request**

---

## 📜 MY OUTING PASSES PAGE

### What You'll See After Submission

```
┌─────────────────────────────────────────────────┐
│         📋 My Outing Passes                     │
│                        [Request New Pass]       │
├─────────────────────────────────────────────────┤
│                                                 │
│  ⏳ PENDING REQUESTS                             │
│  ┌──────────────────────────────────────────┐  │
│  │ 📅 25 Jan 2026 to 27 Jan 2026            │  │
│  │ 3 day(s) | Reason: Family function      │  │
│  │ [Awaiting Approval] badge                │  │
│  │ Requested: 24 Jan 2026 10:30             │  │
│  └──────────────────────────────────────────┘  │
│                                                 │
│  ✅ APPROVED PASSES                             │
│  ┌──────────────────────────────────────────┐  │
│  │ 📅 25 Jan 2026 to 27 Jan 2026            │  │
│  │ 3 day(s) | Reason: Family function      │  │
│  │ [Approved] [By: Admin Name]              │  │
│  │ Approved: 24 Jan 2026 11:00              │  │
│  │ 📧 Guardian Notified                     │  │
│  └──────────────────────────────────────────┘  │
│                                                 │
│  ❌ REJECTED PASSES                             │
│  (None yet)                                     │
│                                                 │
│  [Back to Dashboard]                           │
│                                                 │
└─────────────────────────────────────────────────┘
```

### Status Indicators
- **⏳ Pending** (Yellow) - Waiting for admin review
- **✅ Approved** (Green) - Admin approved, guardian notified
- **❌ Rejected** (Red) - Admin rejected with reason

---

## 👨‍💼 ADMIN DASHBOARD

### Location in Admin UI
```
Admin Dashboard
│
├── Statistics Cards
│   ├── 📊 Total Rooms
│   ├── 📊 Occupied Rooms
│   ├── 📊 Total Students
│   ├── 📊 Open Complaints
│   └── 📊 Total Revenue
│
├── Quick Action Buttons
│   ├── [View Rooms]
│   ├── [Allocate Rooms]
│   ├── [View Complaints]
│   ├── 🚪 [VIEW OUTING REQUESTS] ← NEW BUTTON
│   └── [Django Admin]
│
└── Recent Activity
    └── Recent Complaints
```

### How to Access
**Path 1**: Direct URL
```
http://127.0.0.1:8000/admin-dashboard/
```

**Path 2**: From Dashboard
```
1. Login as admin: admin / admin123
2. Click "Admin Dashboard" button
3. Automatically redirects to Admin Dashboard
```

**Path 3**: Direct to Requests
```
http://127.0.0.1:8000/outing/admin-requests/
```

---

## 🚪 ADMIN OUTING REQUESTS PAGE

### Dashboard Statistics
```
┌──────────────────┬──────────────────┬──────────────────┐
│ ⏳ PENDING       │ ✅ APPROVED      │ ❌ REJECTED      │
│ Count: 2         │ Count: 1         │ Count: 0         │
└──────────────────┴──────────────────┴──────────────────┘
```

### Pending Requests Table
```
┌─────────────────────────────────────────────────────────────┐
│  ⏳ PENDING REQUESTS (2)                                     │
├──┬──────────┬──────────┬──────┬────────┬──────────┬──────────┤
│  │Student   │Roll No   │Dates │Days    │Reason    │Guardian  │
├──┼──────────┼──────────┼──────┼────────┼──────────┼──────────┤
│  │John Doe  │CS/2024/1 │25-27 │3 days │Family fn│parent@ex │
│  │          │          │Jan   │        │          │ample.com │
│  │          │          │      │        │          │          │
│  │Actions: [Approve] [Reject]                                │
├──┼──────────┼──────────┼──────┼────────┼──────────┼──────────┤
│  │Jane Smith│CS/2024/2 │28-30 │3 days │Wedding  │mom@exam  │
│  │          │          │Jan   │        │          │ple.com   │
│  │          │          │      │        │          │          │
│  │Actions: [Approve] [Reject]                                │
└──┴──────────┴──────────┴──────┴────────┴──────────┴──────────┘
```

### Approved Passes Table
```
┌─────────────────────────────────────────────────────────────┐
│  ✅ APPROVED PASSES (1)                                     │
├──┬──────────┬──────────┬───────────┬────────────┬───────────┤
│  │Student   │Dates     │Approved By│Approved On │Notified   │
├──┼──────────┼──────────┼───────────┼────────────┼───────────┤
│  │John Doe  │25-27 Jan │Admin Name │24 Jan 10am │📧 Sent    │
└──┴──────────┴──────────┴───────────┴────────────┴───────────┘
```

### Rejected Passes Table
```
┌─────────────────────────────────────────────────────────────┐
│  ❌ REJECTED PASSES (0)                                     │
│  No rejected passes yet                                     │
└─────────────────────────────────────────────────────────────┘
```

---

## ✅ APPROVE OUTING PASS PAGE

### What Admin Sees When Clicking "Approve"

```
┌─────────────────────────────────────────────────────────────┐
│         ✅ Approve Outing Pass                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ℹ️ When you approve, an email will be sent to guardian    │
│                                                              │
│  📋 REQUEST DETAILS                                         │
│  ┌─────────────────────┬────────────────────────────────┐  │
│  │ Student Name:       │ John Doe                       │  │
│  │ Username:           │ student1                       │  │
│  │ Roll Number:        │ CS/2024/1                      │  │
│  │ Email:              │ john@student.com               │  │
│  │ Guardian Email:     │ parent@example.com             │  │
│  │ Guardian Phone:     │ 9876543210                     │  │
│  └─────────────────────┴────────────────────────────────┘  │
│                                                              │
│  📅 OUTING DETAILS                                          │
│  ┌─────────────────────┬────────────────────────────────┐  │
│  │ From Date:          │ [25 Jan 2026 (Wednesday)]     │  │
│  │ To Date:            │ [27 Jan 2026 (Friday)]        │  │
│  │ Duration:           │ [3 day(s)]                    │  │
│  │ Requested On:       │ 24 Jan 2026 10:30 AM          │  │
│  └─────────────────────┴────────────────────────────────┘  │
│                                                              │
│  📝 REASON FOR OUTING                                       │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Attending family function at home                    │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  📧 GUARDIAN NOTIFICATION PREVIEW                           │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Subject: Outing Pass Approved - John Doe             │  │
│  │ Message: [Full email content shown]                  │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  [Confirm Approval & Send Notification] [Cancel]           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Actions
- ✅ Review all details
- ✅ Preview email
- ✅ Click "Confirm Approval"
- ✅ Email automatically sent
- ✅ Status updated to "Approved"

---

## ❌ REJECT OUTING PASS PAGE

### What Admin Sees When Clicking "Reject"

```
┌─────────────────────────────────────────────────────────────┐
│         ❌ Reject Outing Pass                               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ⚠️  An email will be sent with rejection reason           │
│                                                              │
│  📋 REQUEST DETAILS                                         │
│  [Similar to Approve page showing student details]         │
│                                                              │
│  ❌ REASON FOR REJECTION                                    │
│  [Text Area to enter rejection reason] *Required           │
│  Example: "Insufficient advance notice"                    │
│                                                              │
│  📧 GUARDIAN NOTIFICATION PREVIEW                           │
│  [Shows rejection email that will be sent]                 │
│                                                              │
│  [Confirm Rejection & Send Notification] [Cancel]          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Actions
- ✅ Review request
- ✅ Enter rejection reason (required)
- ✅ Preview rejection email
- ✅ Click "Confirm Rejection"
- ✅ Email sent with reason
- ✅ Status updated to "Rejected"

---

## 📊 COMPLETE FLOW DIAGRAM

```
                    STUDENT JOURNEY
                         ↓
            ┌─────────────────────────────┐
            │  Student Dashboard          │
            │  [Request Outing Pass] ←────┼─ CLICK HERE
            └─────────────────────────────┘
                         ↓
            ┌─────────────────────────────┐
            │  Request Form               │
            │  • From Date                │
            │  • To Date                  │
            │  • Days                     │
            │  • Reason                   │
            │  • Guardian Email           │
            │  [Submit Request]           │
            └─────────────────────────────┘
                         ↓
            ┌─────────────────────────────┐
            │  Status: PENDING            │
            │  (Awaiting Admin Review)    │
            └─────────────────────────────┘
                    ↙          ↖
        ADMIN APPROVES    ADMIN REJECTS
              ↓                ↓
        ┌─────────────┐  ┌──────────────┐
        │  APPROVED ✅ │  │ REJECTED ❌  │
        │             │  │              │
        │  Email Sent │  │  Email Sent  │
        │  + Reason   │  │  + Reason    │
        └─────────────┘  └──────────────┘
              ↓                ↓
        ┌─────────────────────────────┐
        │  Student Views in           │
        │  "My Outing Passes"         │
        │  Section Updated            │
        └─────────────────────────────┘
```

---

## 🔍 NAVIGATION MAP

### Student Navigation
```
Login → Student Dashboard → Click "Request Outing Pass"
                                        ↓
                            Fill form → Submit
                                        ↓
                            Redirects to "My Outing Passes"
                                        ↓
                            View status (Pending/Approved/Rejected)
```

### Admin Navigation
```
Login → Admin Dashboard → Click "View Outing Requests"
                                        ↓
                        See pending/approved/rejected tables
                                        ↓
                    Click "Approve" or "Reject"
                                        ↓
                    Review details → Confirm
                                        ↓
                    Email sent → Status updated
```

---

## 📱 MOBILE VIEW

On mobile phones, you'll see:
- Forms stack vertically
- Calendar date picker appears on tap
- Tables become scrollable
- Buttons adjust size for touch
- All text remains readable
- All functionality preserved

---

## 🎨 COLOR CODING

| Element | Color | Meaning |
|---------|-------|---------|
| **⏳ Pending** | Yellow/Warning | Awaiting action |
| **✅ Approved** | Green/Success | Action completed |
| **❌ Rejected** | Red/Danger | Action denied |
| **ℹ️ Info** | Blue | Important info |
| **⚠️ Warning** | Yellow/Orange | Take care |

---

## ⌨️ KEYBOARD SHORTCUTS

While not implemented yet, future versions could have:
- `Shift+A` → Approve pass
- `Shift+R` → Reject pass
- `Shift+N` → New request

For now, use mouse/touch to navigate.

---

## 🔗 DIRECT LINKS

### For Students
1. Request Pass: `http://127.0.0.1:8000/outing/request/`
2. View Passes: `http://127.0.0.1:8000/outing/my-passes/`

### For Admins
1. Manage Requests: `http://127.0.0.1:8000/outing/admin-requests/`
2. Approve Pass: `http://127.0.0.1:8000/outing/approve/[PASS_ID]/`
3. Reject Pass: `http://127.0.0.1:8000/outing/reject/[PASS_ID]/`

---

## 📖 HELP & SUPPORT

**If you can't find the buttons:**
1. Make sure you're logged in
2. For students: Go to Student Dashboard
3. For admins: Go to Admin Dashboard
4. Look for "Request Outing Pass" (student) or "View Outing Requests" (admin)
5. If not visible, refresh the page

**If forms don't load:**
1. Check internet connection
2. Clear browser cache
3. Try incognito/private browsing
4. Check if server is running

**If emails don't send:**
1. In development, emails print to console
2. Check terminal for email output
3. For production, configure SMTP settings

---

**Now you know exactly where to find every part of the Outing Pass feature!** 🎉

Start exploring by logging in and clicking the outing pass buttons!
