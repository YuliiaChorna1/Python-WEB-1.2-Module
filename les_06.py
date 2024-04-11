
class Singletone(type):
    """
    Singletone metaclass for making singletons
    """

    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)

        return cls.__instances[cls]
    

class Bob(metaclass=Singletone):
    pass


if __name__ == '__main__':
    a = Bob()
    b = Bob()

    print(a is b)
