from abc import ABC, abstractmethod


class NotReadyError(Exception):
    pass


class VendingMachine(ABC):

    def __init__(self):
        self.paid = False
        self.order = None
        self.prepared = False

    def select_order(self, order_key: str):
        self.order = order_key
        return self

    def pay(self, amount: int):
        self.paid = True
        self._prepare()
        return self

    def get_product(self):
        if not self.prepared:
            raise NotReadyError()

        self.prepared = False
        self._return_change()
        return self

    @property
    def state(self):
        return f'Paid: {self.paid}\nOrder: {self.order}\nPrepared: {self.prepared}'

    @abstractmethod
    def _prepare(self):
        self.prepared = True
        self.order = None
        self.paid = False

    def _return_change(self):
        pass


class CoffeeMachine(VendingMachine):

    def _prepare(self):
        print(
            '1. Set the cup',
            '2. Fill in coffee',
            '3. Fill in sugar',
            sep='\n'
        )
        super()._prepare()


class FoodMachine(VendingMachine):
    
    def _prepare(self):
        print(
            '1. Find item',
            '2. Scroll the spring',
            sep='\n'
        )
        super()._prepare()


if __name__ == '__main__':
    coffee_vending_machine = CoffeeMachine()
    coffee_vending_machine.select_order('espresso').pay(1000)  # .get_product()

    machines = [coffee_vending_machine, FoodMachine()]
    for machine in machines:
        print(machine.state)
