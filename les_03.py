# кастомні метакласи

class AttributeGiver(type):

    def __init__(self, name, bases, dct):
        self.x = 100


class Test(metaclass=AttributeGiver):
    pass

print(Test.x)