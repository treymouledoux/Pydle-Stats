#First working solution 156 / 250 chars
r = range(5)
for x in r:
    for y in r:
        c = "white"

        if x+y > 4:
            c = "brown"

        if x + y > 2 and x == 1 or y > 3 and x != 0:
            c = "yellow"

        if y == 0 and x in [0,2]:
            c = "black"

        if (x, y) == (1, 1):
            c = "orange"
        
        pydle(x, y, "", c)