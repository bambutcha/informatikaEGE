from turtle import *
tracer(0)
k = 20
down()
left(90)

back(5*k)
for i in range(2):
    forward(12*k)
    right(90)
    forward(16*k)
    right(90)

up()
forward(3*k)
right(90)
forward(5*k)
left(90)
down()
for i in range(2):
    forward(12*k)
    left(270)
    back((-18)*k)
    right(90)

update()
up()

for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(3,'blue')
home()
