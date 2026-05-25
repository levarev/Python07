from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> None:
        pass

    @abstractmethod
    def revert(self) -> None:
        pass


class Creature(ABC):
    def __init__(self) -> None:
        self.name = ""
        self.type = ""

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        self.name = "Sproutling"
        self.type = "Grass"

    def attack(self) -> str:
        return ("Sproutling uses Vine Whip!")

    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        self.name = "Bloomelle"
        self.type = "Grass/Fairy"

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self) -> str:
        return "Bloomelle heals itself and others for a large amount"


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


class Shiftling(TransformCapability, Creature):
    def __init__(self) -> None:
        self.name = "Shiftling"
        self.type = "Normal"
        self.transformation = False

    def attack(self) -> str:
        if self.transformation is False:
            return "Shiftling attacks normally."
        return "Shiftling performs a boosted strike!"

    def transform(self) -> None:
        self.transformation = True
        print("Shiftling shifts into a sharper form!")

    def revert(self) -> None:
        self.transformation = False
        print("Shiftling returns to normal.")


class Morphagon(TransformCapability, Creature):
    def __init__(self) -> None:
        self.name = "Morphagon"
        self.type = "Normal/Dragon"
        self.transformation = False

    def attack(self) -> str:
        if self.transformation is False:
            return " Morphagon attacks normally."
        return "Morphagon unleashes a devastating morph strike!"

    def transform(self) -> None:
        self.transformation = True
        print("Morphagon morphs into a dragonic battle form!")

    def revert(self) -> None:
        self.transformation = False
        print("Morphagon stabilizes its form.")


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()


class Flameling(Creature):
    def __init__(self) -> None:
        self.name = "Flameling"
        self.type = "Fire"

    def attack(self) -> str:
        return ("Flameling uses Ember!")


class Torragon(Creature):
    def __init__(self) -> None:
        self.name = "Torragon"
        self.type = "Hydro"

    def attack(self) -> str:
        return ("Torragon uses Hydro Pump!")


class Aquabub(Creature):
    def __init__(self) -> None:
        self.name = "Aquabub"
        self.type = "Water"

    def attack(self) -> str:
        return ("Aquabub uses Water Gun!")


class AquaFactory(CreatureFactory):
    def create_base(self) -> Aquabub:
        return Aquabub()

    def create_evolved(self) -> Torragon:
        return Torragon()


class Pyrodon(Creature):
    def __init__(self) -> None:
        self.name = "Pyrodon"
        self.type = "Fire/Flying"

    def attack(self) -> str:
        return ("Pyrodon uses Flamethrower!")


class FlameFactory(CreatureFactory):
    def create_base(self) -> Flameling:
        return Flameling()

    def create_evolved(self) -> Pyrodon:
        return Pyrodon()
