from turtle import *

width(7)
speed(9)
color("green")
begin_fill()
forward(250)
left(90)

forward(250)
left(90)

forward(250)
left(90)

forward(250)
left(90)
end_fill()


forward(95)
color("black")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(250, 250)
pendown()

color("purple")
begin_fill()
right(150)
forward(250)
left(120)
forward(250)
end_fill()

penup()
goto(35, 150)
pendown()
color("white")
begin_fill()
left(120)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
end_fill()

penup()
goto(195, 150)
pendown()
begin_fill()
left(90)
forward(20)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(40)
end_fill()

penup()
goto(-200, 250)
pendown()

color('yellow')
begin_fill()
circle(50)
end_fill()

exitonclick()