from .BaseModelFromDatabase import BaseModel
from datetime import datetime
from peewee import (DateTimeField, TextField, IntegerField)

class ModelExemple(BaseModel):
    
    token = TextField()
    id = TextField()
    type = TextField()
    status = TextField(default="trying")
    attemps = IntegerField(default=0)
    error = TextField(default="")
    created = DateTimeField(default=datetime.now)



