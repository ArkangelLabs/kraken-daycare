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
            "options": "Employee",
            "width": 100,
        },
        {
            "fieldname": "full_name",
            "label": _("Full Name"),
            "fieldtype": "Data",
            "width": 180,
        },
        {
            "fieldname": "role",
            "label": _("Role"),
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "fieldname": "status",
            "label": _("Status"),
            "fieldtype": "Data",
            "width": 100,
        },
        {
            "fieldname": "email",
            "label": _("Email"),
            "fieldtype": "Data",
            "width": 200,
        },
        {
            "fieldname": "phone",
            "label": _("Phone"),
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "fieldname": "hire_date",
            "label": _("Hire Date"),
            "fieldtype": "Date",
            "width": 100,
        },
        {
            "fieldname": "qualification_count",
            "label": _("Qualifications"),
            "fieldtype": "Int",
            "width": 100,
        },
        {
            "fieldname": "expiring_qualifications",
            "label": _("Expiring Soon"),
            "fieldtype": "Int",
            "width": 100,
        },
    ]


def get_data(filters):
    conditions = []
    values = {}

    if filters:
        if filters.get("status"):
            conditions.append("e.status = %(status)s")
            values["status"] = filters.get("status")

        if filters.get("role"):
            conditions.append("e.role = %(role)s")
            values["role"] = filters.get("role")

    where_clause = " AND ".join(conditions) if conditions else "1=1"

    data = frappe.db.sql(
        f"""
        SELECT
            e.name,
            e.full_name,
            e.role,
            e.status,
            e.email,
            e.phone,
            e.hire_date,
            (SELECT COUNT(*) FROM `tabEmployee Qualification` eq WHERE eq.employee = e.name) as qualification_count,
            (SELECT COUNT(*) FROM `tabEmployee Qualification` eq
             WHERE eq.employee = e.name
             AND eq.expiry_date IS NOT NULL
             AND eq.expiry_date <= DATE_ADD(CURDATE(), INTERVAL 30 DAY)
             AND eq.expiry_date >= CURDATE()) as expiring_qualifications
        FROM `tabEmployee` e
        WHERE {where_clause}
        ORDER BY e.full_name
        """,
        values,
        as_dict=True,
    )

    return data
