#!/usr/bin/python3
import json
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        obj_class_name = obj.__class__.__name__
        key = "{}.{}".format(obj_class_name, obj.id)
        FileStorage.__objects[key] = obj
    @classmethod
    def all(cls):
        return FileStorage.__objects
    
    def save(self):
        obj_dict = {}

        for obj_key, obj in FileStorage.__objects.items():
            obj_dict[obj_key] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)

                        instance = cls(**value)
                        FileStorage.__objects[key] = instance
                except Exception as e:
                    pass

