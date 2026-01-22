# Copyright (c) 2025, Daycare Admin and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class Room(Document):
	def validate(self):
		self.validate_age_range()
		self.validate_capacity()

	def validate_age_range(self):
		"""Ensure min age is less than max age"""
		if self.age_range_min_months >= self.age_range_max_months:
			frappe.throw(_("Minimum Age must be less than Maximum Age"))

	def validate_capacity(self):
		"""Ensure capacity is positive"""
		if self.capacity <= 0:
			frappe.throw(_("Capacity must be greater than zero"))

	def update_occupancy(self):
		"""Update current occupancy based on enrolled children"""
		count = frappe.db.count("Child", {
			"room": self.name,
			"enrollment_status": "Enrolled"
		})
		self.db_set("current_occupancy", count, update_modified=False)
