from typing import Callable

l = ["Mon", "tue", "Wed", "Thu", "fri", "sat", "Sun"]


def change_words(words: list[str], func: Callable[[str], str]):
    for word in words:
        print(func(word))


change_words(l, lambda word: word.capitalize())
