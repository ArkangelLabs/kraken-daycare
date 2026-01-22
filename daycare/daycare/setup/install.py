# Copyright (c) 2025, Daycare Admin and contributors
# For license information, please see license.txt

"""
Seed data for Daycare Management System.
Run after app installation to create demo/sample data.
"""

import frappe
from frappe.utils import today, add_months, add_days, getdate
from datetime import date


def after_install():
    """Run after app installation to create seed data."""
    if frappe.flags.in_install or frappe.flags.in_setup_wizard:
        return

    create_roles()
    create_sample_rooms()
    create_sample_groups()
    create_sample_employees()
    create_sample_gnb_rules()
    create_sample_internal_rules()
    create_sample_room_activities()
    frappe.db.commit()
    print("Daycare seed data created successfully!")


def create_roles():
    """Create custom roles for the daycare system."""
    roles = [
        {
            "role_name": "Daycare Admin",
            "desk_access": 1,
            "is_custom": 1,
        },
        {
            "role_name": "Director",
            "desk_access": 1,
            "is_custom": 1,
        },
        {
            "role_name": "Supervisor",
            "desk_access": 1,
            "is_custom": 1,
        },
        {
            "role_name": "Staff",
            "desk_access": 1,
            "is_custom": 1,
        },
    ]

    for role_data in roles:
        if not frappe.db.exists("Role", role_data["role_name"]):
            role = frappe.get_doc({"doctype": "Role", **role_data})
            role.insert(ignore_permissions=True)
            print(f"Created role: {role_data['role_name']}")


def create_sample_rooms():
    """Create sample room records."""
    rooms = [
        {
            "room_name": "Infant Room",
            "capacity": 8,
            "age_range_min_months": 0,
            "age_range_max_months": 12,
            "status": "Active",
            "description": "Room for infants aged 0-12 months. Equipped with cribs, changing stations, and age-appropriate toys.",
        },
        {
            "room_name": "Toddler Room",
            "capacity": 12,
            "age_range_min_months": 12,
            "age_range_max_months": 24,
            "status": "Active",
            "description": "Room for toddlers aged 12-24 months. Features soft play areas and learning stations.",
        },
        {
            "room_name": "Preschool Room A",
            "capacity": 16,
            "age_range_min_months": 24,
            "age_range_max_months": 48,
            "status": "Active",
            "description": "Preschool room for children aged 2-4 years. Includes art stations, reading corner, and outdoor access.",
        },
        {
            "room_name": "Preschool Room B",
            "capacity": 16,
            "age_range_min_months": 48,
            "age_range_max_months": 60,
            "status": "Active",
            "description": "Pre-Kindergarten room for children aged 4-5 years. Focus on school readiness activities.",
        },
    ]

    for room_data in rooms:
        if not frappe.db.exists("Room", {"room_name": room_data["room_name"]}):
            doc = frappe.get_doc({"doctype": "Room", **room_data})
            doc.insert(ignore_permissions=True)
            print(f"Created room: {room_data['room_name']}")


def create_sample_groups():
    """Create sample group records."""
    groups = [
        {
            "group_name": "Little Stars",
            "age_range_min_months": 0,
            "age_range_max_months": 12,
            "max_children": 8,
            "status": "Active",
            "description": "Infant care group focusing on nurturing and developmental milestones.",
        },
        {
            "group_name": "Busy Bees",
            "age_range_min_months": 12,
            "age_range_max_months": 24,
            "max_children": 10,
            "status": "Active",
            "description": "Toddler group with focus on exploration and language development.",
        },
        {
            "group_name": "Creative Cubs",
            "age_range_min_months": 24,
            "age_range_max_months": 36,
            "max_children": 12,
            "status": "Active",
            "description": "Early preschool group focusing on creativity and social skills.",
        },
        {
            "group_name": "Discovery Dragons",
            "age_range_min_months": 36,
            "age_range_max_months": 48,
            "max_children": 14,
            "status": "Active",
            "description": "Preschool group emphasizing discovery and early learning.",
        },
        {
            "group_name": "Ready Rockets",
            "age_range_min_months": 48,
            "age_range_max_months": 60,
            "max_children": 16,
            "status": "Active",
            "description": "Pre-K group preparing children for kindergarten transition.",
        },
    ]

    for group_data in groups:
        if not frappe.db.exists("Group", {"group_name": group_data["group_name"]}):
            doc = frappe.get_doc({"doctype": "Group", **group_data})
            doc.insert(ignore_permissions=True)
            print(f"Created group: {group_data['group_name']}")


def create_sample_employees():
    """Create sample employee records with qualifications."""
    employees = [
        {
            "first_name": "Sarah",
            "last_name": "Johnson",
            "email": "sarah.johnson@daycare.localhost",
            "phone": "506-555-0101",
            "role": "Director",
            "status": "Active",
            "hire_date": add_months(today(), -24),
            "date_of_birth": "1985-03-15",
            "qualifications": [
                {
                    "qualification_type": "Certification",
                    "qualification_name": "Early Childhood Education Diploma",
                    "issuing_authority": "NBCC",
                    "issue_date": "2008-06-01",
                    "expiry_date": "2099-12-31",  # Permanent credential
                    "status": "Active",
                },
                {
                    "qualification_type": "Certification",
                    "qualification_name": "First Aid & CPR",
                    "issuing_authority": "Red Cross",
                    "issue_date": add_months(today(), -10),
                    "expiry_date": add_months(today(), 14),
                    "status": "Active",
                },
            ],
        },
        {
            "first_name": "Michael",
            "last_name": "Chen",
            "email": "michael.chen@daycare.localhost",
            "phone": "506-555-0102",
            "role": "Supervisor",
            "status": "Active",
            "hire_date": add_months(today(), -18),
            "date_of_birth": "1990-07-22",
            "qualifications": [
                {
                    "qualification_type": "Certification",
                    "qualification_name": "Early Childhood Education Certificate",
                    "issuing_authority": "NBCC",
                    "issue_date": "2015-05-01",
                    "expiry_date": "2099-12-31",  # Permanent credential
                    "status": "Active",
                },
                {
                    "qualification_type": "Certification",
                    "qualification_name": "First Aid & CPR",
                    "issuing_authority": "St. John Ambulance",
                    "issue_date": add_months(today(), -6),
                    "expiry_date": add_months(today(), 18),
                    "status": "Active",
                },
            ],
        },
        {
            "first_name": "Emily",
            "last_name": "Rodriguez",
            "email": "emily.rodriguez@daycare.localhost",
            "phone": "506-555-0103",
            "role": "Lead Educator",
            "status": "Active",
            "hire_date": add_months(today(), -12),
            "date_of_birth": "1992-11-08",
            "qualifications": [
                {
                    "qualification_type": "Certification",
                    "qualification_name": "ECE Level II",
                    "issuing_authority": "NB Early Learning",
                    "issue_date": "2018-09-01",
                    "expiry_date": "2099-12-31",  # Permanent credential
                    "status": "Active",
                },
            ],
        },
        {
            "first_name": "David",
            "last_name": "Thompson",
            "email": "david.thompson@daycare.localhost",
            "phone": "506-555-0104",
            "role": "Educator",
            "status": "Active",
            "hire_date": add_months(today(), -6),
            "date_of_birth": "1995-02-28",
            "qualifications": [
                {
                    "qualification_type": "Certification",
                    "qualification_name": "ECE Level I",
                    "issuing_authority": "NB Early Learning",
                    "issue_date": "2020-06-01",
                    "expiry_date": "2099-12-31",  # Permanent credential
                    "status": "Active",
                },
                {
                    "qualification_type": "Certification",
                    "qualification_name": "Criminal Record Check",
                    "issuing_authority": "RCMP",
                    "issue_date": add_months(today(), -6),
                    "expiry_date": add_months(today(), 30),
                    "status": "Active",
                },
            ],
        },
        {
            "first_name": "Lisa",
            "last_name": "Martin",
            "email": "lisa.martin@daycare.localhost",
            "phone": "506-555-0105",
            "role": "Assistant",
            "status": "Active",
            "hire_date": add_months(today(), -3),
            "date_of_birth": "1998-09-10",
            "qualifications": [
                {
                    "qualification_type": "Certification",
                    "qualification_name": "First Aid & CPR",
                    "issuing_authority": "Red Cross",
                    "issue_date": add_months(today(), -2),
                    "expiry_date": add_months(today(), 22),
                    "status": "Active",
                },
            ],
        },
    ]

    for emp_data in employees:
        qualifications = emp_data.pop("qualifications", [])

        if not frappe.db.exists("Employee", {"email": emp_data["email"]}):
            emp = frappe.get_doc({"doctype": "Employee", **emp_data})
            emp.insert(ignore_permissions=True)
            print(f"Created employee: {emp_data['first_name']} {emp_data['last_name']}")

            # Create qualifications
            for qual_data in qualifications:
                qual = frappe.get_doc({
                    "doctype": "Employee Qualification",
                    "employee": emp.name,
                    **qual_data,
                })
                qual.insert(ignore_permissions=True)


def create_sample_gnb_rules():
    """Create sample GNB (Government of New Brunswick) compliance rules."""
    gnb_rules = [
        {
            "regulation_reference": "Reg 83-85, s.12(1)",
            "rule_title": "Staff-to-Child Ratio - Infants",
            "rule_description": "For infants (0-2 years), the staff-to-child ratio must be 1:3.",
            "category": "Staffing Ratios",
            "compliance_status": "Compliant",
            "last_audit_date": add_months(today(), -3),
            "next_audit_date": add_months(today(), 9),
        },
        {
            "regulation_reference": "Reg 83-85, s.12(2)",
            "rule_title": "Staff-to-Child Ratio - Toddlers",
            "rule_description": "For toddlers (2-3 years), the staff-to-child ratio must be 1:5.",
            "category": "Staffing Ratios",
            "compliance_status": "Compliant",
            "last_audit_date": add_months(today(), -3),
            "next_audit_date": add_months(today(), 9),
        },
        {
            "regulation_reference": "Reg 83-85, s.12(3)",
            "rule_title": "Staff-to-Child Ratio - Preschool",
            "rule_description": "For preschool children (3-5 years), the staff-to-child ratio must be 1:7.",
            "category": "Staffing Ratios",
            "compliance_status": "Compliant",
            "last_audit_date": add_months(today(), -3),
            "next_audit_date": add_months(today(), 9),
        },
        {
            "regulation_reference": "Reg 83-85, s.15",
            "rule_title": "Criminal Record Checks",
            "rule_description": "All staff must have a current criminal record check, renewed every 3 years.",
            "category": "Documentation",
            "compliance_status": "Compliant",
            "last_audit_date": add_months(today(), -3),
            "next_audit_date": add_months(today(), 9),
        },
        {
            "regulation_reference": "Reg 83-85, s.18",
            "rule_title": "First Aid Certification",
            "rule_description": "At least one staff member with current first aid certification must be present at all times.",
            "category": "Training",
            "compliance_status": "Compliant",
            "last_audit_date": add_months(today(), -3),
            "next_audit_date": add_months(today(), 9),
        },
        {
            "regulation_reference": "Reg 83-85, s.22",
            "rule_title": "Indoor Space Requirements",
            "rule_description": "Minimum 3.25 square meters of indoor play space per child.",
            "category": "Facilities",
            "compliance_status": "Compliant",
            "last_audit_date": add_months(today(), -3),
            "next_audit_date": add_months(today(), 9),
        },
        {
            "regulation_reference": "Reg 83-85, s.25",
            "rule_title": "Outdoor Play Area",
            "rule_description": "Outdoor play area must be fenced and provide minimum 5.6 square meters per child.",
            "category": "Facilities",
            "compliance_status": "Compliant",
            "last_audit_date": add_months(today(), -3),
            "next_audit_date": add_months(today(), 9),
        },
        {
            "regulation_reference": "Reg 83-85, s.30",
            "rule_title": "Fire Safety Equipment",
            "rule_description": "Fire extinguishers must be inspected annually. Smoke detectors tested monthly.",
            "category": "Safety",
            "compliance_status": "Compliant",
            "last_audit_date": add_months(today(), -1),
            "next_audit_date": add_months(today(), 11),
        },
    ]

    for rule_data in gnb_rules:
        if not frappe.db.exists("GNB Rule", {"regulation_reference": rule_data["regulation_reference"]}):
            doc = frappe.get_doc({"doctype": "GNB Rule", **rule_data})
            doc.insert(ignore_permissions=True)
            print(f"Created GNB Rule: {rule_data['rule_title']}")


def create_sample_internal_rules():
    """Create sample internal daycare rules and policies."""
    internal_rules = [
        {
            "rule_name": "Illness Policy",
            "category": "Health & Safety",
            "description": """Children must be symptom-free for 24 hours before returning to daycare after illness.

Symptoms requiring exclusion:
- Fever over 38°C
- Vomiting or diarrhea
- Contagious illness (pink eye, hand-foot-mouth, etc.)
- Undiagnosed rash""",
            "status": "Active",
            "effective_date": add_months(today(), -12),
            "review_date": add_months(today(), 6),
        },
        {
            "rule_name": "Drop-off and Pick-up Procedures",
            "category": "Health & Safety",
            "description": """Drop-off: 7:00 AM - 9:00 AM
Pick-up: 3:30 PM - 5:30 PM

All children must be signed in/out by authorized adults only.
Photo ID may be requested for unfamiliar authorized pick-up persons.
Late pick-up fee: $1 per minute after 5:30 PM.""",
            "status": "Active",
            "effective_date": add_months(today(), -12),
            "review_date": add_months(today(), 6),
        },
        {
            "rule_name": "Medication Administration",
            "category": "Health & Safety",
            "description": """All medications must:
- Be in original container with child's name
- Have written authorization from parent/guardian
- Include dosage instructions from physician
- Be stored securely

Staff will document all medication administration.""",
            "status": "Active",
            "effective_date": add_months(today(), -12),
            "review_date": add_months(today(), 6),
        },
        {
            "rule_name": "Screen Time Policy",
            "category": "Operations",
            "description": """No screen time for children under 2 years.
Limited educational screen time (max 30 min/day) for children 2+.
All content must be age-appropriate and educational.""",
            "status": "Active",
            "effective_date": add_months(today(), -6),
            "review_date": add_months(today(), 6),
        },
        {
            "rule_name": "Outdoor Play Requirements",
            "category": "Operations",
            "description": """Weather permitting, children will have outdoor play:
- Morning: 9:30 AM - 10:30 AM
- Afternoon: 2:30 PM - 3:30 PM

Indoor alternatives provided during extreme weather (below -20°C or above 30°C with humidex).""",
            "status": "Active",
            "effective_date": add_months(today(), -12),
            "review_date": add_months(today(), 6),
        },
        {
            "rule_name": "Allergy Management Protocol",
            "category": "Health & Safety",
            "description": """All allergies must be documented and communicated to all staff.
Allergy lists posted in each room (without names for privacy).
No nuts or nut products allowed on premises.
EpiPens stored in designated locations with staff trained in administration.""",
            "status": "Active",
            "effective_date": add_months(today(), -12),
            "review_date": add_months(today(), 3),
        },
    ]

    for rule_data in internal_rules:
        if not frappe.db.exists("Internal Rule", {"rule_name": rule_data["rule_name"]}):
            doc = frappe.get_doc({"doctype": "Internal Rule", **rule_data})
            doc.insert(ignore_permissions=True)
            print(f"Created Internal Rule: {rule_data['rule_name']}")


def create_sample_room_activities():
    """Create sample room activities for calendar display."""
    # Get rooms
    rooms = frappe.get_all("Room", pluck="name")
    if not rooms:
        return

    # Daily schedule template (applies to each room)
    daily_schedule = [
        {"activity_type": "Circle Time", "start_time": "08:30:00", "end_time": "09:00:00", "title": "Morning Circle"},
        {"activity_type": "Learning Activity", "start_time": "09:00:00", "end_time": "10:00:00", "title": "Learning Time"},
        {"activity_type": "Meal - Snack", "start_time": "10:00:00", "end_time": "10:30:00", "title": "Morning Snack"},
        {"activity_type": "Outdoor Play", "start_time": "10:30:00", "end_time": "11:30:00", "title": "Outdoor Play"},
        {"activity_type": "Meal - Lunch", "start_time": "11:30:00", "end_time": "12:30:00", "title": "Lunch"},
        {"activity_type": "Nap Time", "start_time": "12:30:00", "end_time": "14:30:00", "title": "Nap Time"},
        {"activity_type": "Meal - Snack", "start_time": "14:30:00", "end_time": "15:00:00", "title": "Afternoon Snack"},
        {"activity_type": "Art & Crafts", "start_time": "15:00:00", "end_time": "16:00:00", "title": "Art & Crafts"},
        {"activity_type": "Free Play", "start_time": "16:00:00", "end_time": "17:00:00", "title": "Free Play"},
    ]

    # Create activities for this week and next week
    current_date = getdate(today())
    # Find Monday of current week
    days_since_monday = current_date.weekday()
    monday = add_days(current_date, -days_since_monday)

    activities_created = 0
    for room in rooms[:2]:  # Just first 2 rooms to avoid too much data
        for week_offset in [0, 7]:  # This week and next week
            for day_offset in range(5):  # Monday to Friday
                activity_date = add_days(monday, week_offset + day_offset)

                for schedule_item in daily_schedule:
                    # Check if activity already exists
                    if frappe.db.exists("Room Activity", {
                        "room": room,
                        "date": activity_date,
                        "activity_type": schedule_item["activity_type"],
                        "start_time": schedule_item["start_time"]
                    }):
                        continue

                    doc = frappe.get_doc({
                        "doctype": "Room Activity",
                        "room": room,
                        "date": activity_date,
                        "activity_type": schedule_item["activity_type"],
                        "start_time": schedule_item["start_time"],
                        "end_time": schedule_item["end_time"],
                        "title": schedule_item["title"],
                        "status": "Scheduled",
                        "all_day": 0,
                    })
                    doc.insert(ignore_permissions=True)
                    activities_created += 1

    if activities_created > 0:
        print(f"Created {activities_created} Room Activities")
