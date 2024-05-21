import frappe
from frappe import _

def before_save(self, method):
    if self.status == "Completed":
        if self.custom_work_to_be_done != self.custom_work_done:
            frappe.throw("Work To Be Done and Work Done Needs to be match to complete the task")
    else:
        frappe.throw(self.status)