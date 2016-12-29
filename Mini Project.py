import turtle

def dt(L, t):
    t.lt(60)
    t.fd(L)
    t.rt(120)
    t.fd(L)
    t.rt(120)
    t.fd(L)
    t.rt(180)

def fractal(L, lv, t):
    if lv ==1:
        dt(L, t)
    else:
        fractal(L/2, lv-1,t)
        t.lt(60)
        t.fd(L/2)
        t.rt(60)
        fractal(L/2, lv-1,t)
        t.rt(60)
        t.fd(L/2)
        t.lt(60)
        fractal(L/2, lv-1,t)
        t.bk(60)

length = float(input("Length: "))
lvl = int(input("Level: "))

window = turtle.Screen()
window.bgcolor("purple")
tu = turtle.Turtle()
tu.speed(100)
tu.color("yellow")
tu.shape("classic")
tu.penup()
tu.goto(-300,-200)
tu.pendown()

fractal(length, lvl, tu)
window.exitonclick()
