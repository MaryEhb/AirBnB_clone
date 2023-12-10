#!/usr/bin/python3
''' file storge module'''
import os.path
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    '''FileStorage class '''
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        '''init of class'''
        pass

    def all(self):
        ''' returns the dictionary __objects '''
        return FileStorage.__objects

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id '''
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        objs = {}
        for [k, v] in FileStorage.__objects.items():
            objs[k] = v.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(objs, f)

    def reload(self):
        ''' deserializes the JSON file to __objects'''
        if os.path.isfile(FileStorage.__file_path):
            if os.path.getsize(FileStorage.__file_path) > 0:
                with open(FileStorage.__file_path) as f:
                    data = json.load(f)
                for [k, v] in data.items():
                    FileStorage.__objects[k] = eval(v["__class__"])(**v)
