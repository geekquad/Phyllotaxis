import math
import turtle

def drawPhyllPattern(turtle, t, petalstart, angle = 137.508, size = 2,
cspread = 4 ):
    """print a pattern of circles using spiral phyllotactic data"""
    # initialize position
    # turtle.pen(outline=1, pencolor="black", fillcolor="orange")
    turtle.color('black')
    turtle.fillcolor("orange")
    phi = angle * ( math.pi / 180.0 ) #we convert to radian
    xcenter = 0.0
    ycenter = 0.0
    # for loops iterate in this case from the first value until < 4,so
    for n in range (0, t):
        r = cspread * math.sqrt(n)
        theta = n * phi
        x = r * math.cos(theta) + xcenter
        y = r * math.sin(theta) + ycenter
        # move the turtle to that position and draw
        turtle.up()
        turtle.setpos(x, y)
        turtle.down()
        # orient the turtle correctly
        turtle.setheading(n * angle)
        if n > petalstart-1:
            turtle.color("yellow")
            drawPetal(turtle, x, y)
        else: turtle.stamp()
def drawPetal(turtle, x, y ):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color('black')
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    turtle.right(20)
    turtle.forward(70)
    turtle.left(40)
    turtle.forward(70)
    turtle.left(140)
    turtle.forward(70)
    turtle.left(40)
    turtle.forward(70)
    turtle.penup()
    turtle.end_fill() # this is needed to complete the last petal
gfg = turtle.Turtle()
gfg.shape("turtle")
gfg.speed(0) # make the turtle go as fast as possible
drawPhyllPattern(gfg, 200, 160, 137.508 )
gfg.penup()
gfg.forward(1000)
