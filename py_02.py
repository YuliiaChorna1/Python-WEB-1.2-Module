# Pattern SINGLETON

class Singleton:
    __instance = None

    def __new__(cls, *args, **kwards):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwards)
        return cls.__instance


if __name__ == '__main__':

    s1 = Singleton()
    s2 = Singleton() # here we made s2 = s1


    print(s1 == s2)
