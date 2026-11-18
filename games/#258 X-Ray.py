#First working solution 93 / 250 chars
r = range(5)
i = 1
for x in r:
    for y in r:
        c = "black"

        if y > 0 and i % 2:
            c = "blue"

        if x == 2:
            c = "white"
        pydle(x, y, "", c)
        i += 1