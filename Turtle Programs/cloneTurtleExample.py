import turtle
t=turtle.Turtle()
c=t.clone()
t.color("Magenta")
c.color("Red")
t.begin_fill()
c.begin_fill()
t.circle(100)
c.circle(60)
t.end_fill()
c.end_fill()
