import turtle

turtle.title('Hello World')

bob = turtle.Turtle()

bob.speed(3)
bob.pensize(10)

bob.getscreen().bgcolor('#C4FCEF')
bob.hideturtle()
bob.color('red')
def pen_goto(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

# draw H
pen_goto(-320, 90)
bob.setheading(90)
bob.forward(90)
pen_goto(-320, 135)
bob.setheading(0)
bob.forward(60)
pen_goto(-260, 90)
bob.setheading(90)
bob.forward(90)

# draw E
pen_goto(-170, 90)
bob.setheading(180)
bob.forward(60)
bob.setheading(90)
bob.forward(90)
bob.setheading(0)
bob.forward(60)
pen_goto(-230, 135)
bob.forward(50)

# draw L
pen_goto(-140, 180)
bob.setheading(270)
bob.forward(90)
bob.setheading(0)
bob.forward(55)

pen_goto(-55, 180)
bob.setheading(270)
bob.forward(90)
bob.setheading(0)
bob.forward(55)

# draw O
pen_goto(60, 90)
bob.circle(45)

# draw W
pen_goto(-100, 0)
bob.right(75)
bob.forward(93)
bob.left(150)
bob.forward(93)
bob.right(150)
bob.forward(93)
bob.left(150)
bob.forward(93)

# draw O
pen_goto(60, -90)
bob.setheading(0)
bob.circle(45)

# draw R
pen_goto(130, -90)
bob.setheading(90)
bob.forward(90)
bob.right(90)
bob.forward(35)
bob.circle(-22,180)
bob.forward(35)
pen_goto(165, -44)
bob.goto(197,-90)

# draw L
pen_goto(227, 0)
bob.setheading(270)
bob.forward(90)
bob.setheading(0)
bob.forward(55)

#draw D
pen_goto(312, -90)
bob.setheading(90)
bob.forward(90)
bob.right(90)
bob.forward(25)
bob.circle(-45,180)
bob.goto(312,-90)

turtle.done()