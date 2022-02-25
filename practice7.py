from __future__ import annotations


class Word:
    def __init__(self, text: str) -> None:
        self.text = text

    def __str__(self) -> str:
        return "Word!!!"

    def __len__(self):
        return len(self.text)

    def __add__(self, word: Word):
        return self.text.lower() + word.text.lower()


w = Word("test")
w2 = Word("##############")

print(w + w2)
