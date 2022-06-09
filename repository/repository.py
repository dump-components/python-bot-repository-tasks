from ..models.task_model import TaskModel
from ..database.task_db import task

class Repository:

    def __init__(self) -> None:
        self.__database = task
        self.connect()
    
    def connect(self):
        try:
            self.__database.connect()
        except Exception as err:
            ValueError(err)
    
    def eliminates_any_chance_of_trying_again(self, task: TaskModel):
        task.attemps = 3
        self.saving_changes_task()
        
    def insert_critical_in_status(self, task: TaskModel):
        task.status = "critical"
        self.saving_changes_task()
    
    def insert_error_in_status(self, task: TaskModel):
        task.status = "error"
        self.saving_changes_task()
    
    def insert_error_message(self, message, task: TaskModel):
        task.error = message
        self.saving_changes_task()
    
    def saving_changes_task(self, task: TaskModel):
        task.save()
    
    def burnt_attempt(self, task: TaskModel):
        task.attemps += 1
        self.saving_changes_task()
        
    @staticmethod
    def verify_attemps(task: TaskModel):
        if task.attemps < 3:
            return True
        raise "Manda erro para api quando todas as tentativas já forem usadas"
    
    def save_task_data_in_database(self, task_data):
        try:
            return TaskModel.insert_many([task_data]).execute(database=self.__database)
        except Exception as err:
             raise err
    
    def select_valid_task(self):
        try:
            task = TaskModel.select().where(TaskModel.status == 'trying').get()
        except:
            return None
        if self.verify_attemps(task):
            return task
    
    def delete_task(self, task: TaskModel):
        task.delete_instance()
