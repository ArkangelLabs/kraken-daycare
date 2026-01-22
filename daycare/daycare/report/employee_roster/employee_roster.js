// Copyright (c) 2025, Daycare Admin and contributors
// For license information, please see license.txt

frappe.query_reports["Employee Roster"] = {
	"filters": [
		{
			"fieldname": "status",
			"label": __("Status"),
			"fieldtype": "Select",
			"options": "\nActive\nOn Leave\nTerminated",
			"default": "Active"
		},
		{
			"fieldname": "role",
			"label": __("Role"),
			"fieldtype": "Select",
			"options": "\nDirector\nSupervisor\nLead Educator\nEducator\nAssistant\nCook\nCleaner\nAdministrator\nOther"
		}
	]
};
