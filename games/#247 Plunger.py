#First working solution 119 / 250 chars
r = range(5)
for x in r:
    for y in r:
        i = x + (y * 5)
        c = "white"
        l = ''

        if x == 2:
            c = "brown"

        if y > 2 and not i in [15, 19]:
            c = "red"

        if i == 3:
            l = '🧤'
        
        pydle(x, y, l, c)