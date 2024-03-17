from turtle import *
tracer(0)
k = 30

left(90)
down()

for i in range(4):
    forward(8*k)
    right(90)
for i in range(4):
    left(30)
    forward(6*k)
    right(30)
    forward(8*k)
    right(150)
    forward(6*k)
    left(60)
update()
up()

for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(3, 'red')


