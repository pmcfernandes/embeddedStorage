import importlib
import json


class FileStorage:
    __file_path = "file.json"
    __temp = importlib.import_module('models')

    def __init__(self):
        """
        Init constructor
        """
        self.__objects = {}

    def all(self):
        """
        Get all objects in list format
        """
        return self.__objects

    def new(self, obj):
        """
        Add new object to list
        """
        string = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[string] = obj

    def save(self):
        """
        Save all objects to file system
        """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as fd:
            json.dump(new_dict, fd)
        pass

    def load(self):
        """
        Load all data from json in filesystem and put all in list
        """
        try:
            with open(self.__file_path, 'r') as fd:
                self.__objects = json.load(fd)

            for key, value in self.__objects.items():
                class_name = key.split(".")[0]
                self.__objects[key] = getattr(self.__temp, class_name)(**value)

        except FileNotFoundError:
            return
