import abc
from typing import Optional


class Person(metaclass=abc.ABCMeta):
    def __init__(self, age: int) -> None:
        self.age = age

    @abc.abstractclassmethod
    def drive(self):
        pass


class Baby(Person):
    def __init__(self, age: int = 1) -> None:
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        return super().drive()


class Adult(Person):
    def __init__(self, age: int = 19) -> None:
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        return super().drive()


class Car:
    def __init__(self, model: Optional[str] = None) -> None:
        self.model = model

    def run(self):
        print("run")

    def ride(self, person: Person):
        person.drive()


baby = Baby()
adult = Adult()


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
