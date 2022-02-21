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

print(1 is True)
