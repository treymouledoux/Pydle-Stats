#First working solution 153 / 250 chars
r = range(5)
for x in r:
    for y in r:
        c = "white"
        l = ""

        if y == 0:
            if x in [0,4]:
                l = "🎵"
            if x == 2:
                c = "orange"

        if y == 1 and 0<x<4 or y == 2:
            c = "yellow"

        if y > 3 or (x,y) == (2,3):
            c = "brown"
    
        pydle(x, y, l, c)