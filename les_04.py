# Abstract factory

from abc import ABC, abstractmethod

class Carry(ABC):
    @abstractmethod
    def run_fast(self):
        pass

class Tank(ABC):
    @abstractmethod
    def hit_hard(self):
        pass

class Support(ABC):
    @abstractmethod
    def heal_nice(self):
        pass

class EnemyFactory(ABC):
    @abstractmethod
    def createTank(self):
        pass

    @abstractmethod
    def createCarry(self):
        pass

    @abstractmethod
    def createSupport(self):
        pass 

class StreetFactory(EnemyFactory):
    def createTank(self):
        return StreetTank()
    
    def createCarry(self):
        return StreetCarry()
    
    def createSupport(self):
        return StreetSupport()
    
class ForestFactory(EnemyFactory):
    def createTank(self):
        return ForestTank()
    
    def createSupport(self):
        return ForestSupport()
    
    def createCarry(self):
        return ForestCarry()
    
class Level:
    def __init__(self, enemy_factory):
        self.enemy_factory = enemy_factory
        self.tanks = []
        ...

    def trap(self):
        for i in range(30):
            self.tanks.append(self.enemy_factory.createTank())
    
    def process(self):
        ...

        for tank in self.tanks:
            tank.hit_hard()
        ...

class StreetTank(Tank):
    def hit_hard(self):
        pass

class StreetCarry(Carry):
    def run_fast(self):
        pass

class StreetSupport(Support):
    def heal_nice(self):
        pass

class ForestTank(Tank):
    def hit_hard(self):
        pass

class ForestCarry(Carry):
    def run_fast(self):
        pass

class ForestSupport(Support):
    def heal_nice(self):
        pass

LEVEL = "forest"

factory = None

if LEVEL == "forest":
    factory = ForestFactory()
elif LEVEL == "street":
    factory = StreetFactory()

Level = Level(factory)