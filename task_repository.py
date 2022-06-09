from .repository.repository import Repository

class TaskRepository:
    
    def get(self):
        return Repository().select_valid_task()
    
    def save(self, task):
        Repository().save_task_data_in_database(task)