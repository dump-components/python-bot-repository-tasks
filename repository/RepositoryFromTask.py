from base_model.BaseModelFromDatabase import sqlite_db, BaseModel


class RepositoryFromTask:
    

    def __init__(self, task_model: BaseModel) -> None:
        self.__database = sqlite_db
        self.__task_model = task_model
        self.__connect()
        self.__create_table()
    
    def save_data_task(self, data_task: dict) -> None:
        try:
            self.__task_model.insert_many([data_task]).execute()
        except Exception as err:
             raise err
    
    def get_task(self) -> BaseModel|None:
        try:
            task =  self.__task_model.select().where(self.__task_model.status == 'trying').get()
        except:
            return None
        if not self.__verify_attemps(task):
            raise ValueError("attempt limits exceeded")
        return task
    
    def eliminates_any_chance_of_trying_again(self) -> None:
        self.__task_model.attemps = 3
        self.__task_model.save()

    def insert_critical_in_status(self) -> None:
        self.__task_model.status = "critical"
        self.__task_model.save()
    
    def insert_error_in_status(self) -> None:
        self.__task_model.status = "error"
        self.__task_model.save()
    
    def insert_error_message(self, message) -> None:
        self.__task_model.error = message
        self.__task_model.save()
    
    def burnt_attempt(self) -> None:
        self.__task_model.attemps += 1
        self.__task_model.save()
        
    def destroy_instance(self, task: BaseModel) -> None:
        task.delete_instance()

    def __connect(self) -> None:
        try:
            self.__database.connect()
        except Exception as err:
            ValueError(err)
    
    def __create_table(self) -> None:
        try:
            self.__database.create_tables(models=[self.__task_model])
        except Exception as err:
            raise err
    
    def __verify_attemps(self, task: BaseModel) -> bool:
        if task.attemps < 3:
            return True