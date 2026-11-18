# import turtle

# # 1. Create the screen and the turtle
# screen = turtle.Screen()
# t = turtle.Turtle()

# # 2. Customize the turtle (optional)
# t.shape("arrow")
# t.color("green")
# t.pensize(3)

# # 3. Draw a simple square
# for _ in range(4):
#     t.forward(100)  # Move forward 100 pixels
#     t.right(90)     # Turn right 90 degrees

# # 4. Keep the window open until you click to close it
# turtle.done()



# # import package
# import turtle 

# # loop for pattern
# for i in range(10):
  
#   # set turtle speed
#   turtle.speed(10-i)
  
#   # motion for pattern
#   turtle.forward(50+10*i)
#   turtle.right(90)

# turtle.done()


# import turtle

# turtle.seth(0)
# turtle.forward(80)
# turtle.write("East")

# turtle.home()
# turtle.setheading(90)
# turtle.forward(80)
# turtle.write("North")

# turtle.home()
# turtle.seth(180)
# turtle.forward(80)
# turtle.write("West", align="right")

# turtle.home()
# turtle.setheading(270)
# turtle.forward(80)
# turtle.write("South", align="left")

# turtle.done()


# import turtle
# import time

# t = turtle.Turtle()

# time.sleep(1)
# t.forward(50)
# t.left(120)

# time.sleep(1)
# t.forward(50)
# t.left(120)
# time.sleep(1)
# t.forward(50)
# time.sleep(1)
# t.right(90)

# turtle.done()


import turtle
import time

print(turtle.position())    
turtle.forward(100)  
print(turtle.position())    

turtle.home()  
print(turtle.position())    

time.sleep(1)
turtle.right(90)  
turtle.forward(100)  
print(turtle.position())    

turtle.home()  
print(turtle.position())    

turtle.done()