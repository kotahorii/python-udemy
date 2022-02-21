from typing import Any

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
