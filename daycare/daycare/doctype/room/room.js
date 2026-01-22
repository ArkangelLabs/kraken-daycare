// Copyright (c) 2025, Daycare and contributors
// For license information, please see license.txt

frappe.ui.form.on("Room", {
    refresh: function(frm) {
        if (!frm.is_new()) {
            // Add button to view Room Activity Calendar
            frm.add_custom_button(__("View Schedule"), function() {
                frappe.set_route("List", "Room Activity", {
                    room: frm.doc.name,
                    view: "Calendar"
                });
            }, __("Actions"));

            // Add button to add new activity
            frm.add_custom_button(__("Add Activity"), function() {
                frappe.new_doc("Room Activity", {
                    room: frm.doc.name
                });
            }, __("Actions"));
        }
    }
});
