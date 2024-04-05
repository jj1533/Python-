import turtle
t=turtle.Turtle()
turtle.bgcolor("black")
t.color("red","blue")
t.begin_fill()
while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos())<1:   #turtle point back at home position
        break
t.end_fill()
t.hideturtle()
turtle.done()
turtle.mainloop()