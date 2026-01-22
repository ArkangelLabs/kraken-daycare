# Copyright (c) 2025, Daycare and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RoomActivity(Document):
    def validate(self):
        self.validate_times()
        self.set_title_if_empty()
        self.set_color_by_activity()

    def validate_times(self):
        """Ensure end time is after start time."""
        if not self.all_day and self.start_time and self.end_time:
            if self.end_time <= self.start_time:
                frappe.throw("End Time must be after Start Time")

    def set_title_if_empty(self):
        """Auto-generate title if not provided."""
        if not self.title:
            self.title = f"{self.activity_type} - {self.room}"

    def set_color_by_activity(self):
        """Set default calendar color based on activity type."""
        if not self.color:
            color_map = {
                "Learning Activity": "#4CAF50",  # Green
                "Outdoor Play": "#8BC34A",       # Light Green
                "Indoor Play": "#CDDC39",        # Lime
                "Nap Time": "#9C27B0",           # Purple
                "Meal - Breakfast": "#FF9800",   # Orange
                "Meal - Lunch": "#FF5722",       # Deep Orange
                "Meal - Snack": "#FFC107",       # Amber
                "Circle Time": "#2196F3",        # Blue
                "Art & Crafts": "#E91E63",       # Pink
                "Music & Movement": "#00BCD4",   # Cyan
                "Story Time": "#3F51B5",         # Indigo
                "Free Play": "#009688",          # Teal
                "Special Event": "#F44336",      # Red
                "Field Trip": "#795548",         # Brown
                "Parent Visit": "#607D8B",       # Blue Grey
                "Other": "#9E9E9E",              # Grey
            }
            self.color = color_map.get(self.activity_type, "#9E9E9E")


@frappe.whitelist()
def get_events(start, end, filters=None):
    """Get Room Activity events for calendar view."""
    from frappe.desk.calendar import get_event_conditions

    conditions = get_event_conditions("Room Activity", filters)

    events = frappe.db.sql(
        """
        SELECT
            name,
            title,
            date as start,
            date as end,
            room,
            activity_type,
            status,
            color,
            all_day,
            start_time,
            end_time,
            assigned_staff
        FROM `tabRoom Activity`
        WHERE date BETWEEN %(start)s AND %(end)s
        {conditions}
        """.format(conditions=conditions),
        {"start": start, "end": end},
        as_dict=True,
    )

    # Combine date and time for proper calendar display
    for event in events:
        if not event.all_day and event.start_time:
            event["start"] = f"{event['start']} {event['start_time']}"
        if not event.all_day and event.end_time:
            event["end"] = f"{event['end']} {event['end_time']}"

    return events
