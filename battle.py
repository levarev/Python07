from ex0.utils import FlameFactory, AquaFactory, CreatureFactory


def call(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def fight(f1: CreatureFactory, f2: CreatureFactory) -> None:
    print("Testing battle")
    first = f1.create_base()
    second = f2.create_base()
    print(first.describe())
    print("vs")
    print(second.describe())
    print(f"{first.attack()}\n{second.attack()}")


if __name__ == '__main__':
    call(FlameFactory())
    print()
    call(AquaFactory())
    print()
    fight(FlameFactory(), AquaFactory())
