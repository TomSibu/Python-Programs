import turtle
t = turtle.Turtle()
t.speed(0)
colors=['red','purple','blue','green','orange','yellow']
for x in range(50):
  t.pencolor(colors[x%6])
  t.forward(x)
  t.right(59)