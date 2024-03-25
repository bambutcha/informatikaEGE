from turtle import *

tracer(0)
k = 35
down()
left(90)

right(120)
for i in range (3):
    right(30)
    forward(6*k)
    right(30)
right(30)
for i in range (3):
    forward(6*k)
    right(60)

update()
up()

for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(3, 'red')     
