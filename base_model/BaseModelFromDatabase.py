from peewee import Model, SqliteDatabase


sqlite_db = SqliteDatabase('.database/task.db')

class BaseModel(Model):
    data_base = sqlite_db
    
    class Meta:
        database = sqlite_db