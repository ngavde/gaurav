// Copyright (c) 2024, MIT and contributors
// For license information, please see license.txt

frappe.query_reports["Timesheet Summary"] = {
	"filters": [
		// {
        //     "fieldname": "from_date",
        //     "label": __("From Date"),
        //     "fieldtype": "Date"
        // },
        // {
        //     "fieldname": "to_date",
        //     "label": __("To Date"),
        //     "fieldtype": "Date"
        // },
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": erpnext.utils.get_fiscal_year(frappe.datetime.get_today(), true)[1],
			"reqd": 1
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": erpnext.utils.get_fiscal_year(frappe.datetime.get_today(), true)[2],
			"reqd": 1
		},
		{
            "fieldname": "project",
            "label": __("Project"),
            "fieldtype": "Link",
			"options": "Project"
        },
		{
            "fieldname": "employee",
            "label": __("Employee"),
            "fieldtype": "Link",
			"options": "Employee"
        },
		{
            "fieldname": "task",
            "label": __("Task"),
            "fieldtype": "Link",
			"options": "Task"
        },
		{
            "fieldname": "project_type",
            "label": __("Project Type"),
            "fieldtype": "Link",
			"options": "Project Type"
        },
		
		{
			fieldname: "range",
			label: __("Range"),
			fieldtype: "Select",
			options: [
				{ "value": "Weekly", "label": __("Weekly") },
				{ "value": "Monthly", "label": __("Monthly") },
				{ "value": "Quarterly", "label": __("Quarterly") },
				{ "value": "Yearly", "label": __("Yearly") }
			],
			default: "Monthly",
			reqd: 1
		}
        // {
		// 	"fieldname": "project_status",
		// 	"fieldtype": "Select",
		// 	"label": "Project Status",
		// 	"options": "Open\Completed\nCancelled"
		// }
		
		
	]
};
