import turtle
import time

# turtle.speed(10)

def draw_petal():
    turtle.circle(50, 180)
    turtle.right(90)
    turtle.circle(50, 180)

for i in range(12):
    draw_petal()
    # time.sleep(1)
    turtle.up()
    # turtle.speed(1)
    turtle.home()
    turtle.down()
    turtle.left(30 * (i+1))

turtle.fillcolor("yellow")
turtle.done()