from ex2.creatures import FlameFactory, AquaFactory
from ex2.creatures import HealingCreatureFactory, TransformCreatureFactory
from ex2.utils import NormalStrategy, AggressiveStrategy
from ex2.utils import DefensiveStrategy, BattleStrategy
from ex2.creatures import Creature


lst = [(FlameFactory().create_base(), NormalStrategy()),
       (HealingCreatureFactory().create_base(), DefensiveStrategy()),
       (FlameFactory().create_base(), AggressiveStrategy()),
       (TransformCreatureFactory().create_base(), AggressiveStrategy())]


def battle(opps: list[tuple[Creature, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opps)} opponents involved")

    for a in range(len(opps)):
        for b in range(a, len(opps)):
            if opps[a] != opps[b]:
                print("\n* Battle *")
                print(opps[a][0].describe())
                print(opps[b][0].describe())
                print("now fight!")
                try:
                    opps[a][1].act(opps[a][0])
                    opps[b][1].act(opps[b][0])
                except Exception as e:
                    print(e)


print("Tournament 0 (basic)")
print("[ (Flameling+Normal), (Healing+Defensive) ]")
battle([lst[0], lst[1]])
print()
print("Tournament 1 (error)")
print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
battle([(FlameFactory().create_base(), AggressiveStrategy()), lst[1]])
print()
print("Tournament 2 (multiple)")
print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
battle([(AquaFactory().create_base(), NormalStrategy()), lst[1], lst[3]])
