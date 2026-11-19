# import package
import turtle

# # method for key call
# def fxn():
#     turtle.forward(40)

# # set turtle screen size
# sc=turtle.Screen()
# sc.setup(600,300)

# # motion
# turtle.forward(40)

# # call method on Right key
# turtle.onkey(fxn,'Right')

# # to listen by the turtle
# turtle.listen()

# # keep the window open until you click to close it


# methods with different work 
# at different keys
def fxn():
    turtle.forward(20)
    
def fxn1():
    turtle.right(90)

def fxn2():
    turtle.left(90)
  
# set screen size
sc=turtle.Screen()
sc.setup(500,300)

# call methods
turtle.onkey(fxn,'space')
turtle.onkey(fxn1,'Right')
turtle.onkey(fxn2,'Left')

# to listen by the turtle
turtle.listen()
turtle.done()