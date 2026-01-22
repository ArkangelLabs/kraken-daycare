# Copyright (c) 2025, Daycare Admin and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import getdate, add_months


class GNBRule(Document):
	def validate(self):
		self.validate_audit_dates()
		self.update_compliance_status_color()

	def validate_audit_dates(self):
		"""Validate that next audit date is after last audit date"""
		if self.last_audit_date and self.next_audit_date:
			if getdate(self.next_audit_date) <= getdate(self.last_audit_date):
				frappe.throw(
					_("Next Audit Date must be after Last Audit Date")
				)

	def update_compliance_status_color(self):
		"""Set indicator color based on compliance status"""
		status_colors = {
			"Compliant": "green",
			"Non-Compliant": "red",
			"Pending Review": "orange",
			"Not Applicable": "grey"
		}
		# This will be used by the frontend indicator

	def is_audit_overdue(self):
		"""Check if audit is overdue"""
		if not self.next_audit_date:
			return False
		return getdate(self.next_audit_date) < getdate()
