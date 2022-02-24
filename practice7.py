from collections import defaultdict

ranking = {"A": 100, "B": 85, "C": 95}
print(sorted(ranking, key=ranking.get, reverse=True))

s = "fdsafdsafdasfdafdasfd"

d: dict[str, int] = defaultdict(int)
for c in s:
    d[c] += 1
print(d)
