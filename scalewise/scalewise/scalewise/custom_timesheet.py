
import frappe
from frappe import _

def on_submit(self, method):
    for row in  self.time_logs:
        if row.custom_todays_work_done:
            task = frappe.get_doc("Task",row.task)
            if task.custom_work_to_be_done < (task.custom_work_done + row.custom_todays_work_done):
                frappe.throw(f"Total work value cannot be greter than {task.custom_work_to_be_done}")
            
            else:
                task.custom_work_done = task.custom_work_done + row.custom_todays_work_done
                task.save()

def on_cancel(self, method):
    for row in  self.time_logs:
        if row.custom_todays_work_done:
            task = frappe.get_doc("Task",row.task)
            task.custom_work_done = task.custom_work_done - row.custom_todays_work_done
            task.save()