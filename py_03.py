# pattern DECORATOR

class Greeting:
    def __init__(self, username) -> None:
        self.username = username

    def greet(self):
        return f"Hello {self.username}"
    


class GreetingDecorator:

    def __init__(self, wrapper) -> None:
        self.wrapper = wrapper

    def greet (self):
        r = self.wrapper.greet()
        return r.upper()

if __name__ == '__main__':
    user = GreetingDecorator(Greeting("Oleh"))
    print(user.greet())