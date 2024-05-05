from turtle import*
tracer(0)
k = 20

left(90)
down()

for i in range(2):
    forward(5*k)
    left(90)
    back(13*k)
    left(90)
up()
back(10*k)
right(90)
forward(9*k)
left(90)
down()
for i in range(2):
    forward(11*k)
    right(90)
    forward(7*k)
    right(90)
update()
up()

for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(5, 'blue')
    
