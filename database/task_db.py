import os
from dotenv import load_dotenv
from peewee import (SqliteDatabase, Model)

load_dotenv()
name_database = "task.db"
dir_database =  os.getenv('DIRECTORY') + "repository\\database\\"
task = SqliteDatabase(dir_database + name_database)

class BaseModel(Model):
    data_base = task
    
    class Meta:
        database = task