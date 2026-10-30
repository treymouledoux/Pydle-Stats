#First working solution 129 / 250 chars
r = range(5)
for x in r:
    for y in r:
        i = x + (y * 5)
        c = "white"

        if y in [1,2] or i == 17:
            c = "brown"

        if i in [7,12]:
            c = "white"

        if i in [20,24]:
            c = "black"

        pydle(x, y, "", c)

#Final Solution 116 / 250 chars
w = "white"
r = range(5)
for x in r:
    for y in r:
        i = x + (y * 5)
        c = w

        if 4 < i < 15 and x != 2 or i == 17:
            c = "brown"

        if i in [20,24]:
            c = "black"

        pydle(x, y, "", c)