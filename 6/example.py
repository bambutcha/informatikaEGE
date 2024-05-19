from turtle import *
k = 30
tracer(0)

down()
left(90)

forward(10*k)
right(90)
forward(10*k)
right(90)
forward(10*k)
right(90)
forward(10*k)

update()
up()
home()

for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(5, 'blue')
