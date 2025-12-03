# Smart Campus Visitor & Gate Access – Requirements (Test Target)

## 1. Background

The Smart Campus Visitor & Gate Access Management System is designed to:
- Control and monitor external visitors entering the campus
- Improve security by enforcing identity verification, time windows, and access rules
- Provide a clear record of who enters and leaves the campus

This document summarizes the **subset of requirements** that will be used as the **test target** in this portfolio project.

---

## 2. Roles

- **Visitor**
  - External person who wants to enter the campus
- **Host**
  - Teacher or staff member who receives the visitor
- **Gate Guard / Gate System**
  - Validates visitor codes and decides whether to open the gate

> In the demo implementation, some roles (like Host, Guard) may be simplified into simple web pages / actions.

---

## 3. Main Features (in scope)

### 3.1 Visitor Booking

**Description:**  
A visitor can submit a visit request through a web form.

**Inputs:**
- Visitor name (required)
- Visitor ID number (simple format, not tied to a real ID system)
- Host name / department (required)
- Visit date and time slot (required, e.g., “2025-12-10 10:00–10:30”)
- Reason for visit (optional)

**Basic Rules:**
1. All required fields must be filled.
2. Visit time must be within allowed campus visiting hours (e.g., 08:00–18:00).
3. Visit time cannot be in the past.

**Output:**
- A booking record with:
  - Booking ID
  - Status = `PENDING`
  - A generated **visitor code** (string, used instead of a QR code)

---

### 3.2 Booking Approval

**Description:**  
The host (or a simplified “admin” in the demo) can approve or reject a booking.

**Rules:**
1. Pending bookings can be:
   - Approved → Status becomes `APPROVED`
   - Rejected → Status becomes `REJECTED`
2. Once approved or rejected, the status cannot be changed again (no further edits).

**Output:**
- Updated booking status
- Visitor code remains the same after approval

---

### 3.3 Gate Access Validation

**Description:**  
At the campus gate, the visitor presents the visitor code. The system decides whether to allow entry.

**Inputs:**
- Visitor code (string) entered in a web form that simulates the gate scanner
- Current time (system time on the server)

**Rules:**
1. The visitor code must exist in the system.
2. The booking status must be `APPROVED`.
3. The current time must be within the allowed visit time window.
4. The visitor must **not** be on a blacklist (demo: a simple in-memory list).
5. If all conditions are met → access is **GRANTED**.
6. Otherwise → access is **DENIED** with a meaningful message:
   - “Booking not found”
   - “Booking not approved”
   - “Visit time window expired”
   - “Visitor is blacklisted”

**Output:**
- A visible result message (GRANTED / DENIED + reason)
- An access log entry (for demo, may just be printed or stored in memory)

---

## 4. Out-of-scope (for this demo)

To keep the project focused on testing, the following aspects are **out of scope**:

- Real QR code generation and scanning
- Real ID card / face recognition integration
- Persistent database (using in-memory or simple JSON storage instead)
- Complex user management and authentication
- Performance / load testing

---

## 5. Constraints and Assumptions

- Time is handled in server local time.
- There is only one campus gate in the demo.
- Blacklist is a simple list of visitor names/IDs defined in the application.
- The goal is to provide a **reasonable and testable** subset of features, not a complete product.

---

## 6. Test Focus

The test scope will focus on:

- Functional correctness of:
  - Booking creation and validation rules
  - Approval status transitions
  - Gate access decision logic
- Boundary conditions for:
  - Visit time window
  - Missing / invalid inputs
  - Blacklist behavior
- End-to-end scenarios:
  - “Happy path”: booking → approval → gate access granted
  - “Unhappy paths”: expired visit, rejected booking, blacklisted visitor, etc.

Details of the test approach, test design techniques, and concrete test cases will be included in:
- `docs/test_plan.md`
- `docs/test_design.md`
- `testcases/` directory
