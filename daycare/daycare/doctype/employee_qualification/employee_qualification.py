# Copyright (c) 2025, Daycare Admin and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import getdate, add_days


class EmployeeQualification(Document):
	def validate(self):
		self.validate_expiry_required()
		self.update_status()

	def validate_expiry_required(self):
		"""Require expiry date for Certification and License types"""
		if self.qualification_type in ("Certification", "License") and not self.expiry_date:
			frappe.throw(
				_("Expiry Date is required for {0} type qualifications").format(
					self.qualification_type
				)
			)

	def update_status(self):
		"""Auto-update status based on expiry date"""
		if not self.expiry_date:
			self.status = "Valid"
			return

		today = getdate()
		expiry = getdate(self.expiry_date)
		days_until_expiry = (expiry - today).days

		if days_until_expiry < 0:
			self.status = "Expired"
		elif days_until_expiry <= 30:
			self.status = "Expiring Soon"
		else:
			self.status = "Valid"
