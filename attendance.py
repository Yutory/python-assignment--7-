"""
Attendance Register

Task:
- Track attendance of students.
- Use a dictionary { "student_id": {"name": str, "present_days": list, "absent_days": list} }
- Functions to mark attendance, check history, and get reports.
- Use your head/logic to mark multiple students at once.
- Use **kwargs for flexible reporting (e.g., only_present=True).

// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Student class with mark_present() and mark_absent().
- AttendanceRegister class that manages records.
"""

import datetime

attendance = {}

def register_student(student_id, name):
    """Register a student in the system."""
    pass

def mark_present(student_ids):
    """Mark multiple students as present for today."""
    today = str(datetime.date.today())
    # implement logic
    pass

def mark_absent(student_ids):
    """Mark multiple students as absent for today."""
    today = str(datetime.date.today())
    #implement logic
    pass

def get_report(**kwargs):
    """Generate attendance report with optional filters."""
    report = {}
    # implement logic

    return report

import datetime

attendance = {}

def register_student(student_id, name):
    """Register a student in the system."""
    if student_id not in attendance:
        attendance[student_id] = {
            "name": name,
            "present_days": [],
            "absent_days": []
        }
    else:
        print(f"Student {student_id} already registered.")


def mark_present(student_ids):
    """Mark multiple students as present for today."""
    today = str(datetime.date.today())
    for sid in student_ids:
        if sid in attendance:
            if today not in attendance[sid]["present_days"]:
                attendance[sid]["present_days"].append(today)
            # remove from absent if mistakenly marked before
            if today in attendance[sid]["absent_days"]:
                attendance[sid]["absent_days"].remove(today)
        else:
            print(f"Student {sid} not registered.")


def mark_absent(student_ids):
    """Mark multiple students as absent for today."""
    today = str(datetime.date.today())
    for sid in student_ids:
        if sid in attendance:
            if today not in attendance[sid]["absent_days"]:
                attendance[sid]["absent_days"].append(today)
            # remove from present if mistakenly marked before
            if today in attendance[sid]["present_days"]:
                attendance[sid]["present_days"].remove(today)
        else:
            print(f"Student {sid} not registered.")


def check_history(student_id):
    """Check full attendance history of a student."""
    if student_id in attendance:
        return attendance[student_id]
    else:
        return f"Student {student_id} not found."


def get_report(**kwargs):
    """
    Flexible reporting:
    - only_present=True  → students present today
    - only_absent=True   → students absent today
    - full=True          → everyone with history
    """
    today = str(datetime.date.today())
    report = {}

    for sid, record in attendance.items():
        if kwargs.get("only_present"):
            if today in record["present_days"]:
                report[sid] = record["name"]
        elif kwargs.get("only_absent"):
            if today in record["absent_days"]:
                report[sid] = record["name"]
        elif kwargs.get("full"):
            report[sid] = record

    return report

register_student("S1", "Alice")
register_student("S2", "Bob")
register_student("S3", "Charlie")

mark_present(["S1", "S2"])
mark_absent(["S3"])

print("Full Report:", get_report(full=True))
print("Only Present Today:", get_report(only_present=True))
print("Only Absent Today:", get_report(only_absent=True))
print("Alice’s History:", check_history("S1"))

