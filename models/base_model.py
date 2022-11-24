#!/usr/bin/python3
""" The base model for other attibutes and intances """
import uuid
from datetime import datetime

class BaseModel():
    """ Define all other attibutes/instances """
    
    id = str(uuid.uuid4())
    date_format = "%Y-%m-%dT%H:%M:%S.%f"
    created_at  = datetime.now()
    updated_at = datetime.now()

    def __str__(self):
        """ Print the class name, id, and __dict__"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ Update the the updated with the current date time """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Set the dict containing all keys/values of __dict__ of the instance """
        the_dict = self.__dict__.copy()
        the_dict["__class__"] = self.__class__.__name__
        the_dict["updated_at"] = self.updated_at.isoformat()
        the_dict["created_at"] = self.created_at.isoformat()
        return (the_dict)
