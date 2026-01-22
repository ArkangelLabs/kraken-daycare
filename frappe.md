# Frappe Development Notes

## Changing Workspace Sidebar Icons

In Frappe v16+, the sidebar uses `Workspace Sidebar` and `Workspace Sidebar Item` doctypes.

### Via Bench Console

```bash
docker exec -i -w /workspace/development/frappe-bench devcontainer-frappe-1 \
  bench --site daycare.localhost console
```

```python
import frappe

# Define icon mapping (link_to doctype -> icon name)
icons = {
    'Employee': 'users',
    'Child': 'smile',
    'Room': 'home',
    'Group': 'users',
    'Employee Qualification': 'award',
    'Internal Rule': 'book',
    'GNB Rule': 'alert-circle',
    'Child Intake Request': 'file-text',
    'Room Activity': 'calendar'
}

# Update sidebar
sidebar = frappe.get_doc('Workspace Sidebar', 'Daycare Admin')
for item in sidebar.items:
    if item.link_to in icons:
        item.icon = icons[item.link_to]
sidebar.save()

frappe.db.commit()
```

### Via API (curl)

```bash
# Get current sidebar
curl -s 'http://daycare.localhost:8000/api/resource/Workspace%20Sidebar/Daycare%20Admin' \
  -H "Authorization: token API_KEY:API_SECRET"

# Update sidebar item icon
curl -X PUT 'http://daycare.localhost:8000/api/resource/Workspace%20Sidebar%20Item/ITEM_NAME' \
  -H "Authorization: token API_KEY:API_SECRET" \
  -H "Content-Type: application/json" \
  -d '{"icon": "users"}'
```

### Available Icons

Icons use [Lucide](https://lucide.dev/icons/) icon names:

| Icon | Name |
|------|------|
| 👤 | `user`, `users` |
| 🏠 | `home` |
| 📅 | `calendar` |
| 📄 | `file-text` |
| 📚 | `book` |
| 🏆 | `award` |
| ⚠️ | `alert-circle` |
| 😊 | `smile` |
| ⚙️ | `settings` |
| 📊 | `bar-chart` |

Full list: https://lucide.dev/icons/

### Clear Cache After Changes

```bash
docker exec -w /workspace/development/frappe-bench devcontainer-frappe-1 \
  bench --site daycare.localhost clear-cache
```

Then hard refresh browser (Cmd+Shift+R / Ctrl+Shift+R).

## Key Doctypes

| DocType | Purpose |
|---------|---------|
| `Workspace` | Main workspace config (shortcuts, links, content) |
| `Workspace Sidebar` | Sidebar menu for a workspace |
| `Workspace Sidebar Item` | Individual sidebar link with `icon` field |
| `Workspace Link` | Links in workspace content (icon only for Card Break type) |
| `Workspace Shortcut` | Shortcut buttons on workspace |

## Checking Sidebar Structure

```python
# Get sidebar with all items
frappe.get_doc('Workspace Sidebar', 'Daycare Admin').as_dict()

# List all sidebars
frappe.get_all('Workspace Sidebar', fields=['name'])

# Check item icons
[(i.label, i.icon, i.link_to) for i in frappe.get_doc('Workspace Sidebar', 'Daycare Admin').items]
```
