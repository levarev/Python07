from ex1.utils import HealingCreatureFactory
from ex1.utils import TransformCreatureFactory


def call(heal: HealingCreatureFactory,
         transform: TransformCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    sproutling = heal.create_base()
    print("base:")
    print(sproutling.describe())
    print(sproutling.attack())
    print(sproutling.heal())
    print("evolved:")
    bloomelle = heal.create_evolved()
    print(bloomelle.describe())
    print(bloomelle.attack())
    print(bloomelle.heal())
    print()
    print("Testing Creature with transform capability")
    shiftling = transform.create_base()
    morphagon = transform.create_evolved()
    print("base")
    print(shiftling.describe())
    print(shiftling.attack())
    shiftling.transform()
    print(shiftling.attack())
    shiftling.revert()
    print("evolved")
    print(morphagon.describe())
    print(morphagon.attack())
    morphagon.transform()
    print(morphagon.attack())
    morphagon.revert()


if __name__ == '__main__':
    call(HealingCreatureFactory(), TransformCreatureFactory())
