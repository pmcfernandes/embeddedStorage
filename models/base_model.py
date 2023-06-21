from datetime import datetime
import uuid
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        """ Init function """
        if 'id' in kwargs:
            self.id = kwargs['id']
        else:
            self.id = str(uuid.uuid4())
            models.storage.new(self)

        if 'created_at' in kwargs:
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
        else:
            self.created_at = datetime.now()

        if 'updated_at' in kwargs:
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.updated_at = datetime.now()

    def __str__(self):
        """ toString function """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Save model to storage """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Convert model to dict"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
