#First working solution 132 / 250 chars
r = range(5)
for x in r:
    for y in r:
        i = x + (y * 5)
        c = "white"
        l = ''

        if x+y == 3:
            c = "blue"

        if x+y == 5:
            c = "red"

        if x in [0,4]:
            c = "black"

        if i in [2,22]:
            l = 'I'

        pydle(x, y, l, c)

#Final Solution 130 / 250 chars
i = 0
r = range(5)
for y in r:
    for x in r:
        c = "white"
        l = ''

        if x+y == 3:
            c = "blue"

        if x+y == 5:
            c = "red"

        if x in [0,4]:
            c = "black"

        if i in [2,22]:
            l = 'I'

        pydle(x, y, l, c)
        i += 1