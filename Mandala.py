from turtle import *
import colorsys

speed(0)
bgcolor('black')
hue = 0.0
hideturtle()
pensize()

for i in range(185):
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    pencolor(color)
    circle(190-i, 90)
    lt(90)
    circle(190-i, 90)
    lt(10)
    hue += 0.005
mainloop()


# Love You baby!!!
# perechi go sona, perechi!
# aamra perechi!
