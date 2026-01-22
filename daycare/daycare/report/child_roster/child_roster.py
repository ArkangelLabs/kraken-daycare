# Copyright (c) 2025, Daycare Admin and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    return [
        {
            "fieldname": "name",
            "label": _("ID"),
            "fieldtype": "Link",
            "options": "Child",
            "width": 100,
        },
        {
            "fieldname": "full_name",
            "label": _("Child Name"),
            "fieldtype": "Data",
            "width": 180,
        },
        {
            "fieldname": "age_months",
            "label": _("Age (Months)"),
            "fieldtype": "Int",
            "width": 100,
        },
        {
            "fieldname": "enrollment_status",
            "label": _("Status"),
            "fieldtype": "Data",
            "width": 100,
        },
        {
            "fieldname": "group_name",
            "label": _("Group"),
            "fieldtype": "Data",
            "width": 140,
        },
        {
            "fieldname": "room_name",
            "label": _("Room"),
            "fieldtype": "Data",
            "width": 140,
        },
        {
            "fieldname": "enrollment_date",
            "label": _("Enrolled"),
            "fieldtype": "Date",
            "width": 100,
        },
        {
            "fieldname": "primary_guardian",
            "label": _("Primary Guardian"),
            "fieldtype": "Data",
            "width": 160,
        },
        {
            "fieldname": "guardian_phone",
            "label": _("Guardian Phone"),
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "fieldname": "has_allergies",
            "label": _("Allergies"),
            "fieldtype": "Data",
            "width": 80,
        },
    ]


def get_data(filters):
    conditions = []
    values = {}

    if filters:
        if filters.get("enrollment_status"):
            conditions.append("c.enrollment_status = %(enrollment_status)s")
            values["enrollment_status"] = filters.get("enrollment_status")

        if filters.get("group"):
            conditions.append("c.group = %(group)s")
            values["group"] = filters.get("group")

        if filters.get("room"):
            conditions.append("g.room = %(room)s")
            values["room"] = filters.get("room")

    where_clause = " AND ".join(conditions) if conditions else "1=1"

    data = frappe.db.sql(
        f"""
        SELECT
            c.name,
            c.full_name,
            c.age_months,
            c.enrollment_status,
            c.enrollment_date,
            g.group_name,
            r.room_name,
            (SELECT cg.guardian_name FROM `tabChild Guardian` cg
             WHERE cg.parent = c.name AND cg.is_primary = 1 LIMIT 1) as primary_guardian,
            (SELECT cg.phone FROM `tabChild Guardian` cg
             WHERE cg.parent = c.name AND cg.is_primary = 1 LIMIT 1) as guardian_phone,
            CASE WHEN c.allergies IS NOT NULL AND c.allergies != '' THEN 'Yes' ELSE 'No' END as has_allergies
        FROM `tabChild` c
        LEFT JOIN `tabGroup` g ON c.group = g.name
        LEFT JOIN `tabRoom` r ON g.room = r.name
        WHERE {where_clause}
        ORDER BY c.full_name
        """,
        values,
        as_dict=True,
    )

    return data
