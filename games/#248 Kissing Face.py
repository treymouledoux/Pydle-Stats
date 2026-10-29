#First working solution 168 / 250 chars
r = range(5)
for x in r:
    for y in r:
        c = "yellow"
        l = ''

        if y < 1 and 1 - x % 2:
            c = "black"

        if x < 1 and y in [0,4]:
            c = "white"

        if x+y in [6,8]:
            c = "red"

        if (x,y) == (2,4):
            c = "yellow"

        if (x,y) == (4,3):
            l = '💕'
        
        pydle(x, y, l, c)

#Final Solution 140 / 250 chars
r = range(5)
for x in r:
    for y in r:
        i = x + (y * 5)
        c = "yellow"
        l = ''

        if i in [2,4]:
            c = "black"

        if i in [0,20]:
            c = "white"

        if i in [14, 18, 24]:
                c = "red"

        if i == 19:
            l = '💕'
        
        pydle(x, y, l, c)