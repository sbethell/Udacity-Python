import turtle

#draws letter S
def draw_initial_s(myTurtle):
    myTurtle.up()
    myTurtle.setpos(-100,-50)
    myTurtle.down()
    myTurtle.forward(50)
    myTurtle.left(90)
    myTurtle.forward(50)
    myTurtle.left(90)
    myTurtle.forward(50)
    myTurtle.right(90)
    myTurtle.forward(50)
    myTurtle.right(90)
    myTurtle.forward(50)

#draws letter E
def draw_initial_e(myTurtle):
    myTurtle.up()
    myTurtle.setpos(0,-50)
    myTurtle.down()
    myTurtle.forward(50)
    myTurtle.setpos(0,-50)
    myTurtle.left(90)
    myTurtle.forward(50)
    myTurtle.right(90)
    myTurtle.forward(50)
    myTurtle.setpos(0,0)
    myTurtle.left(90)
    myTurtle.forward(50)
    myTurtle.right(90)
    myTurtle.forward(50)
    

#draws letter B
def draw_initial_b(myTurtle):
    myTurtle.up()
    myTurtle.setpos(100,-50)
    myTurtle.down()
    myTurtle.left(90)
    myTurtle.forward(100)
    myTurtle.right(90)
    myTurtle.forward(50)
    myTurtle.right(90)
    myTurtle.forward(50)
    myTurtle.right(90)
    myTurtle.forward(50)
    myTurtle.left(90)
    myTurtle.forward(50)
    myTurtle.left(90)
    myTurtle.forward(50)
    myTurtle.left(90)
    myTurtle.forward(50)
    
#initialises the window & turtle. hen runs the drawing functions, hides turtle, waits for click    
def main():
    window = turtle.Screen()
    brad = turtle.Turtle()
    brad.color('green')
    brad.speed(10)

    draw_initial_s(brad)
    draw_initial_e(brad)
    draw_initial_b(brad)
    brad.hideturtle()
    
    window.exitonclick()


main()
    
