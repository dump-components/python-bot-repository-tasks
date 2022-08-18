from base_model.BaseModelFromDatabase import BaseModel, sqlite_db

class RepositoryFromTask:

    def __init__(self) -> None:
        self.database = sqlite_db
        self.connect()

    @staticmethod
    def create_table(database, task: BaseModel):
        database.create_tables(models=[task])
    
    def connect(self):
        try:
            self.database.connect()
        except Exception as err:
            ValueError(err)

    @staticmethod
    def verify_attemps(task: BaseModel):
        if task.attemps < 3:
            return True
        raise ValueError("attempt limits exceeded")
    
    @staticmethod
    def save_data(self, data_task):
        try:
            return BaseModel.insert_many([data_task]).execute()
        except Exception as err:
             raise err
    
    @staticmethod
    def select_valid_task():
        try:
            return BaseModel.select().where(BaseModel.status == 'trying').get()
        except Exception as err:
            raise BufferError(err)
    
    @staticmethod
    def eliminates_any_chance_of_trying_again(task: BaseModel):
        task.attemps = 3
        task.save()

    @staticmethod    
    def insert_critical_in_status(task: BaseModel):
        task.status = "critical"
        task.save()
    
    @staticmethod
    def insert_error_in_status(task: BaseModel):
        task.status = "error"
        task.save()
    
    @staticmethod
    def insert_error_message(message, task: BaseModel):
        task.error = message
        task.save()
    
    @staticmethod
    def burnt_attempt(task: BaseModel):
        task.attemps += 1
        task.save()
        
    @staticmethod
    def destroy_instance(task: BaseModel):
        del task
