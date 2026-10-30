#First working solution 79 / 250 chars
r = range(5)
for x in r:
    for y in r:
        c = "yellow"

        if x % 2:
            c = "white"

        if y > 0:
            c = "red"

        pydle(x, y, "", c)

#Final Solution 74 / 250 chars
for i in range(25):
    c = "yellow"

    if i % 2:
        c = "white"

    if i > 4:
        c = "red"

    pydle(i % 5, i // 5, "", c)