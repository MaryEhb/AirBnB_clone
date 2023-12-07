#!/usr/bin/python3
"""BaseModel"""
import uuid
from datetime import datetime, date
import models


class BaseModel:
    """
    BaseModel that defines all common attributes/methods
    for other classes
    """

    def __init__(self, *args, **kwargs):
        """Executed when an instance is initialized"""

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    format = '%Y-%m-%dT%H:%M:%S.%f'
                    date_obj = datetime.strptime(value, format)
                    setattr(self, key, date_obj)
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Return a string representation of the object"""
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        """
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict
