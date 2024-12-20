import sqlite3
from DataAccessLayer import database_name
from Common.Entities.task import Task


class TaskDataAccess:
    def get_task(self):
        task_list = []
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            SELECT id,
            title,
            task,
            start_date,
            end_date,
            status_id
            FROM Tasks""")

            data = cursor.fetchall()

            for item in data:
                task = Task(*item)
                task_list.append(task)

        return task_list
