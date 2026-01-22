// Copyright (c) 2025, Daycare Admin and contributors
// For license information, please see license.txt

frappe.query_reports["Child Roster"] = {
	"filters": [
		{
			"fieldname": "enrollment_status",
			"label": __("Enrollment Status"),
			"fieldtype": "Select",
			"options": "\nActive\nWaitlisted\nGraduated\nWithdrawn\nSuspended",
			"default": "Active"
		},
		{
			"fieldname": "group",
			"label": __("Group"),
			"fieldtype": "Link",
			"options": "Group"
		},
		{
			"fieldname": "room",
			"label": __("Room"),
			"fieldtype": "Link",
			"options": "Room"
		}
	]
};
