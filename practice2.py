from typing import Callable, Generator, Optional

l = ["Mon", "tue", "Wed", "Thu", "fri", "sat", "Sun"]


def change_words(words: list[str], func: Callable[[str], str]):
    for word in words:
        print(func(word))


change_words(l, lambda word: word.capitalize())

l = ["Good morning", "Good afternoon", "Good night"]

for i in l:
    print(i)

print("#######################")


def greeting() -> Generator[str, None, None]:
    yield "Good morning"
    yield "Good afternoon"
    yield "Good night"


for g in greeting():
    print(g)


def counter(num: int = 10) -> Generator[str, None, None]:
    for _ in range(num):
        yield "run"


g = greeting()
c = counter()

print(next(g))
print(next(c))
print(next(g))

t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9, 10)

r = [i * j for i in t for j in t2]
print(r)

w = ["mon", "tue", "wed"]
f = ["coffee", "milk", "water"]

d = {x: y for x, y in zip(w, f)}
print(d)

g = (i for i in range(10))
print(type(g))

l = [1, 2, 3]
i = 5
try:
    l[i]
except IndexError as exc:
    print(f"Don't worry: {exc}")
