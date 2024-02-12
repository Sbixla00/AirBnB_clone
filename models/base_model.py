import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage
from datetime import datetime, timezone

class BaseModel:
    all_id = []
    all_instances = {}

    def __init__(self, *args, **kwargs):
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)
        BaseModel.all_id.append(self.id)
        BaseModel.all_instances[self.id] = self

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, date_format))
                else:
                    setattr(self, key, value)

        FileStorage().new(self)
    def save(self):
        self.updated_at = datetime.utcnow()
        FileStorage.save(self)

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    @classmethod
    def get_instance_by_id(cls, obj_id):
        return cls.all_instances.get(obj_id)

