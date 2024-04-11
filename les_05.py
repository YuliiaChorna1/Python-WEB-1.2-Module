# Factory method

from abc import ABC, abstractmethod

class Level(ABC):
    @abstractmethod
    def activate_physics(self):
        pass

    @abstractmethod
    def generate_biome(self):
        pass

class StreetLevel(Level):
    def activate_physics(self):
        self.gravity = 9.8

    def generate_biome(self):
        self.generate_trees()
        self.generate_oceans()
    ...

class MoonLevel(Level):
    def activate_physics(self):
        self.gravity = 1.6

    def generate_biome(self):
        self.generate_rocks()
    ...

class EngineCreator:
    @abstractmethod
    def factory_method(self):
        pass

    def game_loop(self):
        while True:
            level = self.factory_method()

            level.activate_physics()
            level.generate_biome()

class StreetGameCreator(EngineCreator):
    def factory_method(self):
        return StreetLevel()
    
class MoonGameCreator(EngineCreator):
    def factory_method(self):
        return MoonLevel()

moon_game = MoonGameCreator()
moon_game.game_loop()

street_game = StreetGameCreator()
street_game.game_loop()