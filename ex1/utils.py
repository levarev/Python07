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


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class HealCapability(ABC):
    @abstractmethod
    def heal(self):
        pass


class TransformCapability(ABC):
    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def revert(self):
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
    def __init__(self):
        self.name = "Shiftling"
        self.type = "Normal"
        self.transformation = False

    def attack(self):
        if self.transformation is False:
            return "Shiftling attacks normally."
        return "Shiftling performs a boosted strike!"

    def transform(self):
        self.transformation = True
        print("Shiftling shifts into a sharper form!")

    def revert(self):
        self.transformation = False
        print("Shiftling returns to normal.")


class Morphagon(TransformCapability, Creature):
    def __init__(self):
        self.name = "Morphagon"
        self.type = "Normal/Dragon"
        self.transformation = False

    def attack(self):
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
