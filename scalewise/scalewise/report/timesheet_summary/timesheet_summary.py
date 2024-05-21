# Copyright (c) 2024, MIT and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe import _, scrub
from frappe.utils import add_days, add_to_date, flt, getdate

from erpnext.accounts.utils import get_fiscal_year

def __init__(self, filters=None):
		self.filters = frappe._dict(filters or {})
		self.date_field = (
			"act_start_date"
		)
		self.months = [
			"Jan",
			"Feb",
			"Mar",
			"Apr",
			"May",
			"Jun",
			"Jul",
			"Aug",
			"Sep",
			"Oct",
			"Nov",
			"Dec",
		]
		self.get_period_date_ranges()

def execute(filters=None):
	filters = frappe._dict(filters or {})
	columns = get_columns(filters)
	data = get_data(filters)
	return columns, data

def get_columns(filters):
	columns = [
		{
			"label": _("Timesheet"),
			"fieldtype": "Link",
			"fieldname": "name",
			"options": "Timesheet",
			"width": 100,
		},
		{
			"label": _("Employee"),
			"fieldtype": "Link",
			"fieldname": "employee",
			"options": "Employee",
			"width": 100,
		},
		{
			"label": _("Employee Name"),
			"fieldtype": "Data",
			"fieldname": "employee_name",
			"width": 100,
		},
		{
			"label": _("From Time"),
			"fieldtype": "Datetime",
			"fieldname": "from_time",
			"width": 100,
		},
		{
			"label": _("Activity Type"),
			"fieldtype": "Data",
			"fieldname": "activity_type",
			"width": 100,
		},
		{
			"label": _("Task"),
			"fieldtype": "Link",
			"fieldname": "task",
			"options": "Task",
			"width": 100,
		},
		{
			"label": _("Task"),
			"fieldtype": "Data",
			"fieldname": "task_name",
			"width": 100,
		},

		{
			"fieldname": "task_status",
			"fieldtype": "Select",
			"label": "Task Status",
			"options": "Open\Working\nPending Review\nOverdue\nTemplate\nCompleted\nCancelled",
			"width": 100,
		},
		{
			"label": _("Total Work To Be Done"),
			"fieldtype": "Int",
			"fieldname": "custom_total_work_to_be_done",
			"width": 100,
		},
		{
			"label": _("Work Done Till Date"),
			"fieldtype": "Int",
			"fieldname": "custom_work_done_till_dae",
			"width": 100,
		},
		{
			"label": _("Todays Work Done"),
			"fieldtype": "Int",
			"fieldname": "custom_todays_work_done",
			"width": 100,
		},
		{
			"label": _("Remaining Work"),
			"fieldtype": "Int",
			"fieldname": "remaining_task_work",
			"width": 100,
		},
		{
			"label": _("Task Percentage"),
			"fieldtype": "Float",
			"fieldname": "task_percentage",
			"width": 100,
		},

		{
			"label": _("Project"),
			"fieldtype": "Link",
			"fieldname": "project",
			"options": "Project",
			"width": 100,
		},
		{
			"label": _("Project Name"),
			"fieldtype": "Data",
			"fieldname": "project_name",
			"width": 100,
		},
		{
			"fieldname": "project_status",
			"fieldtype": "Select",
			"label": "Project Status",
			"options": "Open\nCompleted\nCancelled",
			"width": 100,
		},
		
		{
			"fieldname": "percent_complete",
			"fieldtype": "Percentage",
			"label": "Project % Completed",
			"options": "Open\nCompleted\nCancelled",
			"width": 100,
		}
		
	]

	return columns

def get_conditions(filters):
	conditions = f"and task.act_start_date between '{filters.from_date}' and '{filters.to_date}' "

	# if filters.from_date:
	# 	conditions += "and ",filters.from_date
		
	# if filters.to_date:
	# 	conditions["to_date"] = filters.to_date
	
	if filters.project is not None:
		conditions += f"and tri.project = '{filters.project}' "
	
	if filters.project_type is not None:
		conditions += f"and project.project_type = '{filters.project}' "

	if filters.task is not None:
		conditions += f"and tri.task = '{filters.task}' "

	if filters.employee is not None:
		conditions += f"and ti.employee = '{filters.employee}' "

	print(":::::::::::::::;;filter:::::::::::::::",filters.from_date, filters.to_date)

	return conditions


def get_data(filters):
	data = []
	conditions = get_conditions(filters)
	print("conditions-------------------------",conditions)
	data  = frappe.db.sql("""
		SELECT
			ti.name AS 'Timesheet ID',
			ti.employee AS 'Employee',
			ti.employee_name AS 'Employee Name',
			tri.from_time AS 'From Datetime',
			tri.activity_type AS 'Activity Type',
			tri.task AS 'Task',
			task.subject as 'Task Name',
			task.status as 'Task Status',	   
			tri.custom_total_work_to_be_done AS 'Total Work',
			tri.custom_work_done_till_dae AS 'Work Already Done',
			tri.custom_todays_work_done as 'Todays Work Done',
			tri.custom_total_work_to_be_done - (tri.custom_todays_work_done + tri.custom_work_done_till_dae) as 'Remaining Work',
			((tri.custom_work_done_till_dae+tri.custom_todays_work_done)/task.custom_work_to_be_done)*100 as task_percentage,
			tri.project AS 'Project',
			project.project_name as 'Project Name',
			project.status as 'Project Status',
			project.percent_complete as 'Project % Completed'
		FROM
			`tabTimesheet` AS ti
		JOIN
			`tabTimesheet Detail` AS tri ON ti.name = tri.parent
		JOIN
			`tabTask` AS task ON tri.task = task.name
		JOIN
			`tabProject` AS project ON tri.project = project.name
		WHERE
			ti.docstatus = 1 
			 {0}
    """.format(conditions))

	return data 

def get_period_date_ranges(self):
	from dateutil.relativedelta import MO, relativedelta

	from_date, to_date = getdate(self.filters.from_date), getdate(self.filters.to_date)

	increment = {"Monthly": 1, "Quarterly": 3, "Half-Yearly": 6, "Yearly": 12}.get(
		self.filters.range, 1
	)

	if self.filters.range in ["Monthly", "Quarterly"]:
		from_date = from_date.replace(day=1)
	elif self.filters.range == "Yearly":
		from_date = get_fiscal_year(from_date)[1]
	else:
		from_date = from_date + relativedelta(from_date, weekday=MO(-1))

	self.periodic_daterange = []
	for dummy in range(1, 53):
		if self.filters.range == "Weekly":
			period_end_date = add_days(from_date, 6)
		else:
			period_end_date = add_to_date(from_date, months=increment, days=-1)

		if period_end_date > to_date:
			period_end_date = to_date

		self.periodic_daterange.append(period_end_date)

		from_date = add_days(period_end_date, 1)
		if period_end_date == to_date:
			break