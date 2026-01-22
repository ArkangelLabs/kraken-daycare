# Copyright (c) 2025, Daycare Admin and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import getdate, today


class ChildIntakeRequest(Document):
	def before_insert(self):
		if not self.submitted_on:
			self.submitted_on = today()

	def validate(self):
		self.validate_child_age()

	def validate_child_age(self):
		"""Validate that child's date of birth is reasonable"""
		if self.child_date_of_birth:
			dob = getdate(self.child_date_of_birth)
			today_date = getdate(today())

			# Child should not be born in the future
			if dob > today_date:
				frappe.throw(_("Child's date of birth cannot be in the future"))

			# Child should be under 6 years old (typical daycare age limit)
			age_months = (today_date.year - dob.year) * 12 + (today_date.month - dob.month)
			if age_months > 72:  # 6 years
				frappe.msgprint(
					_("Note: Child appears to be over 6 years old. Please verify the date of birth."),
					indicator="orange"
				)

	def on_update(self):
		"""Track who reviewed the intake request"""
		if self.has_value_changed("status") and self.status in ("Under Review", "Approved", "Declined", "Waitlisted"):
			if not self.reviewed_by:
				self.db_set("reviewed_by", frappe.session.user, update_modified=False)
			if not self.reviewed_on:
				self.db_set("reviewed_on", today(), update_modified=False)
