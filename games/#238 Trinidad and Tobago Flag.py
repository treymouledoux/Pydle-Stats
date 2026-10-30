#First working solution 90 / 250 chars
r = range(5)
for x in r:
    for y in r:
        c = "red"

        if x == y:
            c = "black"
        if x - 1 == y or x + 1 == y:
            c = "white"

        pydle(x, y, "", c)