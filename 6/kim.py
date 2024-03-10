import turtle as t

k = 15
t.up()
for x in range(-20,10):
    for y in range(-20,10):
        t.goto(x* k,y * k)
        t.dot()
t.down()

t.home
t.left(90)
t.down()
for i in range(2):
    t.forward(24* k)
    t.right(90)
    t.forward(22* k)
    t.right(90)
t.up()
t.forward(10* k)
t.right(90)
t.back(2* k)
t.left(90)
t.down()
for g in range(2):
    t.forward(3* k)
    t.right(90)
    t.forward(17* k)
    t.right(90)

t.done()


