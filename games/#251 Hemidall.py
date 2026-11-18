#First working solution 127 / 250 chars
r = range(5)
b = [(2, "red"), (5, "yellow"), (7, "blue"), (9, "purple")]

for x in r:
    for y in r:
        d = x + (4 - y)
        c = next(col for l, col in b if d < l)
        pydle(x, y, "", c)