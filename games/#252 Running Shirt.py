#First working solution 96 / 250 chars
r = range(5)
for x in r:
    for y in r:
        c = "green"

        if x+y in [4,5]:
            c = "yellow"

        if y < 2 and 1 - x % 2:
            c = "black"

        pydle(x, y, "", c)