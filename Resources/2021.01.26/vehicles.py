class Engine:

    def __init__(self, hp: int):
        self.hp = hp


class CarEngine(Engine):
    pass


class Vehicle:

    def __init__(self, model: str, year: int):
        self.model = model
        self.year = year
        self.engine = None

    def __repr__(self) -> str:
        return f'{self.model} {self.year} {self.engine.hp}HP'

    def set_engine(self, engine: Engine):
        self.engine = engine


class Car(Vehicle):

    def __init__(self, model: str, year: int):
        super().__init__(model, year)

    def set_engine(self, engine: CarEngine):
        if not isinstance(engine, CarEngine):
            raise TypeError('Not a car engine')
        super().set_engine(engine)


class Bike(Vehicle):
    
    def __init__(self, model: str, year: int):
        super().__init__(model, year)


if __name__ == '__main__':
    my_car = Car('Totota Corolla', 2016)
    my_car.set_engine(CarEngine(118))
    print(my_car)

    my_bike = Bike('Bandit', 2006)
    my_bike.set_engine(Engine(200))
    print(my_bike)
