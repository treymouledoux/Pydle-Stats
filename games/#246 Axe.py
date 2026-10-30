#First working solution 116 / 250 chars
r = range(5)
for x in r:
    for y in r:
        i = x + (y*5)
        c = ""

        if x > 2:
            c = "brown"

        if 3 > y > 0 or i in [1,16]:
            c = "red"

        if x < 1 and y < 4:
            c = "white"
            
        pydle(x, y, "", c)