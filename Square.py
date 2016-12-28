import turtle

def draw_shape():
    window = turtle.Screen()
    window.bgcolor("red")

    draw_triangle()
    draw_square()
    draw_circle()
    

    window.exitonclick()
    
def draw_square():
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(5)
    
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    
def draw_circle():
    
    mort = turtle.Turtle()
    mort.shape("arrow")
    mort.color("black")
    mort.circle(100)

    
def draw_triangle():
    
    colt = turtle.Turtle()
    colt.shape("classic")
    colt.color("blue")

    colt.forward(100)
    colt.left(120)
    colt.forward(100)
    colt.left(120)
    colt.forward(100)
    colt.left(120)

draw_shape()
