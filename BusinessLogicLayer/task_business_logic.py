from DataAccessLayer.tasks_data_access import TaskDataAccess


class TaskBusinessLogic:
    def __init__(self):
        self.task_data_access = TaskDataAccess()

    def get_task_list(self, current_task):
        user_list = self.task_data_access.get_task(current_task.id)
        return user_list