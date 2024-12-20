from ttkbootstrap import Treeview, PRIMARY
from BusinessLogicLayer.task_business_logic import TaskBusinessLogic


class Frame1:

    def __init__(self, frame):
        self.row_list = []
        self.task_business = TaskBusinessLogic()

        self.treeview = Treeview(frame, columns=("", "title", "task", "start_date", "end_date", "status"),
                                 bootstyle=PRIMARY)
        self.treeview.grid(row=0, column=0, sticky="nsew")
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        self.treeview.column("#0", width=40)
        self.treeview.heading("#0", text="NO")
        self.treeview.heading("#1", text="Title")
        self.treeview.heading("#2", text="Task")
        self.treeview.heading("#3", text="Start Date")
        self.treeview.heading("#4", text="End Date")
        self.treeview.heading("#5", text="Status")

    def load_data(self, task_list):
        for row in self.row_list:
            self.treeview.delete(row)

        self.row_list.clear()

        row_number = 1
        for task in task_list:
            row = self.treeview.insert("", "end", idd=task.id, text=str(row_number),
                                       values=(task.title, task.task, task.start_date, task.end_date, task.status_id))
            self.row_list.append(row)
            row_number += 1
