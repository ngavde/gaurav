app_name = "scalewise"
app_title = "Scalewise"
app_publisher = "MIT"
app_description = "Scalewise"
app_email = "MIT@support.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/scalewise/css/scalewise.css"
# app_include_js = "/assets/scalewise/js/scalewise.js"

# include js, css files in header of web template
# web_include_css = "/assets/scalewise/css/scalewise.css"
# web_include_js = "/assets/scalewise/js/scalewise.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "scalewise/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "scalewise/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "scalewise.utils.jinja_methods",
# 	"filters": "scalewise.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "scalewise.install.before_install"
# after_install = "scalewise.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "scalewise.uninstall.before_uninstall"
# after_uninstall = "scalewise.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "scalewise.utils.before_app_install"
# after_app_install = "scalewise.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "scalewise.utils.before_app_uninstall"
# after_app_uninstall = "scalewise.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "scalewise.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Timesheet": {
		"on_submit": "scalewise.scalewise.custom_timesheet.on_submit",
        "on_cancel": "scalewise.scalewise.custom_timesheet.on_cancel"
	},
    "Task": {
		"before_save": "scalewise.scalewise.custom_task.before_save"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"scalewise.tasks.all"
# 	],
# 	"daily": [
# 		"scalewise.tasks.daily"
# 	],
# 	"hourly": [
# 		"scalewise.tasks.hourly"
# 	],
# 	"weekly": [
# 		"scalewise.tasks.weekly"
# 	],
# 	"monthly": [
# 		"scalewise.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "scalewise.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "scalewise.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "scalewise.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["scalewise.utils.before_request"]
# after_request = ["scalewise.utils.after_request"]

# Job Events
# ----------
# before_job = ["scalewise.utils.before_job"]
# after_job = ["scalewise.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"scalewise.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

