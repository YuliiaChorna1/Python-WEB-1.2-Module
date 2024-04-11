from les_06 import Singletone
import json

class Config(metaclass=Singletone):
    def __init__(self, config_file=None):
        print("Loading file...")

        # with open(config_file) as config:
        #     self.data = json.load(config)
        self.data = {"data": "abc"}

    def get_data(self):
        return self.data
    
def a():
    config = Config()
    print(config.data)

def b():
    config = Config()
    print(config.data)

config = Config("abc.json")

a()
b()