from typing import Any, Callable

s = (
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
)

word = "python"
word = "j" + word[1:]
print(word)
print(word.startswith("j"))
print(word.count("t"))
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[::2])
print(list[::-1])

d = {"x": 10, "y": 20}
print(d.keys())
print(d.items())

my_friends = {"A", "C", "D"}
A_friends = {"B", "D", "E", "F"}

print(my_friends & A_friends)

count = 0

while count < 5:
    print(count)
    count += 1
else:
    print("done")

days = ["Mon", "Tue", "Wed"]
fruits = ["apple", "banana", "orange"]
drinks = ["coffee", "tea", "beer"]

for day, fruits, drink in zip(days, fruits, drinks):
    print(day, fruits, drink)


def say_something(word: str, *args: tuple[Any]):
    print("word = ", word)
    for arg in args:
        print(arg)


t = ("Mike", "Nancy")
say_something("Hi!", *t)


def outer(a: int, b: int) -> None:
    def plus(c: int, d: int) -> int:
        return c + d

    print(plus(a, b))


outer(10, 29)


def outer(a: int, b: int) -> Callable[..., int]:
    def inner() -> int:
        return a + b

    return inner


f = outer(1, 2)
r = f()
print(r)


def circle_area_func(pi: float):
    def circle_area(radius: int):
        return pi * radius ** 2

    return circle_area


cal1 = circle_area_func(3.14)
cal2 = circle_area_func(3.141592)

print(cal1(10))


def print_info(func: Callable[[int, int], int]):
    def wrapper(*args: int, **kwargs: int):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result

    return wrapper


@print_info
def add_num(a: int, b: int):
    return a + b


r = add_num(10, 20)
print(r)

# f = print_info(add_num)
# r = f(10, 20)
# print(r)
