# Copyright (c) 2025, Daycare Admin and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class Group(Document):
	def validate(self):
		self.validate_age_range()
		self.validate_max_children()

	def validate_age_range(self):
		"""Ensure min age is less than max age"""
		if self.age_range_min_months >= self.age_range_max_months:
			frappe.throw(_("Minimum Age must be less than Maximum Age"))

	def validate_max_children(self):
		"""Ensure max children is positive"""
		if self.max_children <= 0:
			frappe.throw(_("Maximum Children must be greater than zero"))
