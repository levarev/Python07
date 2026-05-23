from abc import ABC, abstractmethod
from .creatures import Creature
from .creatures import TransformCapability, HealCapability


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, Creature):
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature):
        if self.is_valid(creature) is True:
            print(creature.attack())
        else:
            raise Exception(f"Battle error, aborting tournament:"
                            f" Invalid Creature "
                            f"'{creature.__class__.__name__}' "
                            f"for this normal strategy")


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature):
        if self.is_valid(creature) is True:
            creature.transform()
            print(creature.attack())
            creature.revert()
        else:
            raise Exception(f"Battle error, aborting tournament:"
                            f" Invalid Creature "
                            f"'{creature.__class__.__name__}' "
                            f"for this aggressive strategy")


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature):
        if self.is_valid(creature) is True:
            print(creature.attack())
            print(creature.heal())
        else:
            raise Exception(f"Battle error, aborting tournament:"
                            f" Invalid Creature "
                            f"'{creature.__class__.__name__}' "
                            f"for this defensive strategy")
