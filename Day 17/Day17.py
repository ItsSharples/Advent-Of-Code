


minY = -105
maxY = -57

minX = 206
maxX = 250

# minY = -10
# maxY = -5

# minX = 20
# maxX = 30

def lerp(a, b, t):
    return a + (b-a) * t

out = []
# Using n(n+1)/2
#   we can tell that x must be more than 20 to ever reach the area
#   The stop is then just a number high enough that there are less steps than
#   Stop-Start
for vX in range(20, 260):
# For y, we start at minY, because the first step could complete the task
#   And we end at -minY, because that's the velocity that gets it the highest
    for vY in range(-105, 105):
        x, y = 0, 0
        veloX, veloY = vX, vY
        while True:
            x += veloX
            y += veloY
            veloX += 1 if veloX < 0 else (-1 if veloX > 0 else 0)
            veloY -= 1

            if minX <= x and x <= maxX:
                if maxY >= y and y >= minY:
                    out.append((x,y))
                    break
            if minY > y or maxX < x:
                break

print(len(out))