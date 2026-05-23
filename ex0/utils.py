from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self) -> None:
        self.name = ""
        self.type = ""

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    def __init__(self) -> None:
        self.name = "Flameling"
        self.type = "Fire"

    def attack(self) -> str:
        return ("Flameling uses Ember!")


class Pyrodon(Creature):
    def __init__(self) -> None:
        self.name = "Pyrodon"
        self.type = "Fire/Flying"

    def attack(self) -> str:
        return ("Pyrodon uses Flamethrower!")


class Aquabub(Creature):
    def __init__(self) -> None:
        self.name = "Aquabub"
        self.type = "Water"

    def attack(self) -> str:
        return ("Aquabub uses Water Gun!")


class Torragon(Creature):
    def __init__(self) -> None:
        self.name = "Torragon"
        self.type = "Hydro"

    def attack(self) -> str:
        return ("Torragon uses Hydro Pump!")


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Flameling:
        return Flameling()

    def create_evolved(self) -> Pyrodon:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Aquabub:
        return Aquabub()

    def create_evolved(self) -> Torragon:
        return Torragon()
