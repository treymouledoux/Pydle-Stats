#First working solution 141 / 250 chars
r = range(5)
for x in r:
    for y in r:
        i = y*5 + x
        c = "white"
        l = ""

        if y in [0,4] or x+y == 4:
            c = "blue"

        if x in [0,4]:
            c = "white"

        if i in [6,18]:
            l = "💤"

        if i in [7,17]:
            l = "🛌"
        
        pydle(x, y, l, c)

#Final Solution 136 / 250 chars
p = [0,4]
w = "white"
r = range(5)
for x in r:
    for y in r:
        i = y * 5 + x
        c = w
        l = ""

        if y in p or x+y == 4:
            c = "blue"

        if x in p:
            c = w

        if i in [6,7,17,18]:
            l = "💤"
            if i % 2:
                l = "🛌"
        
        pydle(x, y, l, c)