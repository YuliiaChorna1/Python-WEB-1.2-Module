# Metaclass

class Person:

    def __init__(self, weight) -> None:
        self.weight = weight

    def walk(self):
        print(f"Weight {self.weight} is moving")


def same_person_init(self, weight):
    self.weight = weight

def same_person_walk(self):
    print(f"Weight {self.weight} is moving")

SamePerson = type(
    "Person", (),
    {
        "__init__": same_person_init,
        "walk": same_person_walk
    }
)

dima = Person(70)
denis = SamePerson(75)

dima.walk()
denis.walk()

print(dima)
print(denis)