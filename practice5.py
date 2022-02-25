from typing import Optional


class Person:
    def __init__(self, age: int) -> None:
        self.age = age

    def drive(self):
        if self.age > 18:
            print("ok")
        else:
            raise Exception("No drive")


class Baby(Person):
    def __init__(self, age: int = 1) -> None:
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError


class Adult(Person):
    def __init__(self, age: int) -> None:
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError


class Car:
    def __init__(self, model: Optional[str] = None) -> None:
        self.model = model

    def run(self):
        print("run")

    def ride(self, person: Person):
        person.drive()


class ToyotaCar(Car):
    def run(self):
        print("fast")


class TeslaCar(Car):
    def __init__(
        self, model: Optional[str], enable_auto_run: bool = False, password: int = 123
    ) -> None:
        super().__init__(model=model)
        self._enable_auto_run = enable_auto_run
        self.password = password

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable: bool):
        if self.password == 456:
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def auto_run(self):
        print("auto run")


tesla_car = TeslaCar("Model S", password=456)
tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)
