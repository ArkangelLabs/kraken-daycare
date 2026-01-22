# Copyright (c) 2025, Daycare Admin and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import getdate, nowdate


class Child(Document):
	def before_save(self):
		self.compute_full_name()
		self.compute_age_months()

	def validate(self):
		self.validate_guardians()

	def compute_full_name(self):
		"""Compute full name from first and last name"""
		self.full_name = f"{self.first_name} {self.last_name}".strip()

	def compute_age_months(self):
		"""Compute age in months from date of birth"""
		if not self.date_of_birth:
			self.age_months = 0
			return

		today = getdate(nowdate())
		dob = getdate(self.date_of_birth)

		# Calculate months difference
		months = (today.year - dob.year) * 12 + (today.month - dob.month)

		# Adjust if we haven't reached the birth day this month
		if today.day < dob.day:
			months -= 1

		self.age_months = max(0, months)

	def validate_guardians(self):
		"""Validate that at least one guardian exists and one is primary"""
		if not self.child_guardians:
			frappe.throw(_("At least one guardian is required"))

		primary_count = sum(1 for g in self.child_guardians if g.is_primary)

		if primary_count == 0:
			frappe.throw(_("At least one guardian must be marked as primary contact"))

		if primary_count > 1:
			frappe.throw(_("Only one guardian can be marked as primary contact"))
