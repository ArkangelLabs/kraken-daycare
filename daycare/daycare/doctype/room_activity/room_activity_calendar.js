frappe.views.calendar["Room Activity"] = {
    field_map: {
        start: "date",
        end: "date",
        id: "name",
        title: "title",
        allDay: "all_day",
        color: "color"
    },
    gantt: false,
    filters: [
        {
            fieldtype: "Link",
            fieldname: "room",
            options: "Room",
            label: __("Room")
        },
        {
            fieldtype: "Select",
            fieldname: "activity_type",
            options: "\nLearning Activity\nOutdoor Play\nIndoor Play\nNap Time\nMeal - Breakfast\nMeal - Lunch\nMeal - Snack\nCircle Time\nArt & Crafts\nMusic & Movement\nStory Time\nFree Play\nSpecial Event\nField Trip\nParent Visit\nOther",
            label: __("Activity Type")
        },
        {
            fieldtype: "Select",
            fieldname: "status",
            options: "\nScheduled\nIn Progress\nCompleted\nCancelled",
            label: __("Status")
        }
    ],
    get_events_method: "daycare.daycare.doctype.room_activity.room_activity.get_events"
};
