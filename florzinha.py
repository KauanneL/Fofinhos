from turtle import *
from math import *

speed(0)
bgcolor("black")
goto(0,-40)

# Desenhar folhas
for i in range(16):
    for j in range(18):
        color('#FFA216'), rt(90)
        circle(150-j*6, 90), lt(90)
        circle(150-j*6,90), rt(180)
    circle(40,24)

# Desenhar folhas no centro
color('black')
shape('circle')
shapesize(0.5)
fillcolor('#884513')
golden_ang = 137.508
phi = golden_ang*(pi/180)

for i in range(140):
    r = 4*sqrt(i)
    