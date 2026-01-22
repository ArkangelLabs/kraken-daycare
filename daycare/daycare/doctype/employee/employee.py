# Copyright (c) 2025, Daycare Admin and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class Employee(Document):
	def before_save(self):
		self.compute_full_name()

	def validate(self):
		self.validate_availability()
		self.validate_termination_date()

	def compute_full_name(self):
		"""Compute full name from first and last name"""
		self.full_name = f"{self.first_name} {self.last_name}".strip()

	def validate_availability(self):
		"""Check for overlapping availability entries"""
		if not self.employee_availability:
			return

		for i, row1 in enumerate(self.employee_availability):
			for j, row2 in enumerate(self.employee_availability):
				if i >= j:
					continue

				if row1.weekday != row2.weekday:
					continue

				# Check if time ranges overlap
				if self._times_overlap(row1, row2):
					# Check if date ranges overlap (if specified)
					if self._dates_overlap(row1, row2):
						frappe.throw(
							_("Row {0} and Row {1}: Overlapping availability for {2}").format(
								i + 1, j + 1, row1.weekday
							)
						)

	def _times_overlap(self, row1, row2):
		"""Check if two time ranges overlap"""
		# Convert times to comparable format
		start1 = row1.start_time
		end1 = row1.end_time
		start2 = row2.start_time
		end2 = row2.end_time

		# Check for overlap: ranges overlap if one starts before the other ends
		return start1 < end2 and start2 < end1

	def _dates_overlap(self, row1, row2):
		"""Check if two date ranges overlap (if dates are specified)"""
		# If no dates specified, assume always applicable (overlap)
		if not row1.effective_from and not row2.effective_from:
			return True

		# If one has dates and other doesn't, they could overlap
		if not row1.effective_from or not row2.effective_from:
			return True

		# Both have start dates - check for overlap
		start1 = row1.effective_from
		end1 = row1.effective_to or frappe.utils.getdate("2099-12-31")
		start2 = row2.effective_from
		end2 = row2.effective_to or frappe.utils.getdate("2099-12-31")

		return start1 <= end2 and start2 <= end1

	def validate_termination_date(self):
		"""Validate termination date if status is Terminated"""
		if self.status == "Terminated" and not self.termination_date:
			frappe.throw(_("Termination Date is required when status is Terminated"))
