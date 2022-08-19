from peewee import (Model, SqliteDatabase)


sqlite_db = SqliteDatabase('database/task.db')

class BaseModel(Model):
    database = sqlite_db
    
    class Meta:
        database = sqlite_db