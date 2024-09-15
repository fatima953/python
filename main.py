import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
poligon = turtle.Turtle()
sides = 6
angle = 360 / sides
lenth = 70

for i in range(sides):
    poligon.forward(lenth)
    poligon.right(angle)