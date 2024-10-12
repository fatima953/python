import turtle

t = turtle.Turtle()

# Create a new screen for the turtle and set the background color
screen = turtle.Screen()
screen.bgcolor("sky blue")

# Set the turtle color, shape, and speed
t.color("red")
t.shape("turtle")
t.speed(4)

# Draw the base of the house
t.fillcolor("light pink" )
t.begin_fill()
t.right(90)    # turn the turtle right by 90 degrees
t.forward(250) # move the turtle forward by 250 units
t.left(90)     # turn the turtle left by 90 degrees
t.forward(400) # move the turtle forward by 400 units
t.left(90)     # turn the turtle left by 90 degrees
t.forward(250) # move the turtle forward by 250 units
t.left(90)     # turn the turtle left by 90 degrees
t.forward(400) # move the turtle forward by 400 units
t.right(90)    # turn the turtle right by 90 degrees
t.end_fill()   # end the fill color

# Draw the top of the house
t.fillcolor('yellow')
t.begin_fill()
t.right(45)    # turn the turtle right by 45 degrees
t.forward(200) # move the turtle forward by 200 units
t.right(90)    # turn the turtle right by 90 degrees
t.forward(200) # move the turtle forward by 200 units
t.left(180)    # turn the turtle left by 180 degrees
t.forward(200) # move the turtle forward by 200 units
t.right(135)   # turn the turtle right by 135 degrees
t.forward(259) # move the turtle forward by 259 units
t.right(90)    # turn the turtle right by 90 degrees
t.forward(142) # move the turtle forward by 142 units
t.end_fill()   # end the fill color

# Draw the door and windows
t.right(90)    # turn the turtle right by 90 degrees
t.forward(400) # move the turtle forward by 400 units
t.left(90)     # turn the turtle left by 90 degrees
t.forward(50)  # move the turtle forward by 50 units
t.left(90)     # turn the turtle left by 90 degrees
t.forward(150) # move the turtle forward by 150 units
t.right(90)    # turn the turtle right by 90 degrees
t.forward(200) # move the turtle forward by 200 units
t.right(180)   # turn the turtle left by 180 degrees
t.forward(200) # move the turtle forward by 200 units
t.right(90)    # turn the turtle right by 90 degrees
t.forward(200) # move the turtle forward by 200 units
t.right(90)    # turn the turtle right by 90 degrees
t.forward(150) # move the turtle forward by 150 units
t.right(90)    # turn the turtle right by 90 degrees
t.forward(200) # move the turtle forward by 200 units
t.right(90)    # turn the turtle right by 90 degrees
t.forward(150) # move the turtle forward by 150 units
t.right(90)    # turn the turtle right by 90 degrees
t.forward(100) # move the turtle forward by 100 units

t.right(90) # turn the turtle right by 90 degrees
t.forward(150) # move the turtle forward by 150 units
t.right(90) # turn the turtle right by 90 degrees
t.forward(100) # move the turtle forward by 100 units
t.right(90) # turn the turtle right by 90 degrees
t.forward(75) # move the turtle forward by 75 units
t.right(90) # turn the turtle right by 90 degrees
t.forward(200) # move the turtle forward by 200 units
t.right(180) # turn the turtle left by 180 degrees
t.forward(200) # move the turtle forward by 200 units
t.right(90) # turn the turtle right by 90 degrees
t.forward(75) # move the turtle forward by 75 units
t.left(90) # turn the turtle left by 90 degrees
t.forward(15) # move the turtle forward by 15 units
t.left(90) # turn the turtle left by 90 degrees
t.forward(200) # move the turtle forward by 200 units
t.right(90) # turn the turtle right by 90 degrees
t.forward(15) # move the turtle forward by 15 units
t.right(90) # turn the turtle right by 90 degrees
t.forward(100) # move the turtle forward by 100 units

turtle.done()