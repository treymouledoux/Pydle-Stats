#First working solution 92 / 250 chars
r = range(5)
for x in r:
    for y in r:
        i = x + (y * 5)
        c = "red"

        if i in [0,4,20,24] or 10 < i < 14:
            c = "white"
        
        pydle(x, y, "", c)

#Final Solution 81 / 250 chars
r = range(25)
for i in r:
        c = "red"

        if i in [0,4,20,24] or 10 < i < 14:
            c = "white"
        
        pydle(i%5, i // 5, "", c)