import turtle

emo = turtle.Turtle()

#to make center of circle -- face of emoji

emo.up()
emo.goto(0,-100)
emo.down()

#fill yellow color in circle

emo.begin_fill()
emo.pendown()
emo.fillcolor('yellow')
emo.circle(100)
emo.end_fill()

#semicircle smile in emoji

emo.up()
emo.goto(-64,-40)
emo.setheading(-60)
emo.width(5)
emo.down()
emo.circle(80,120)
emo.fillcolor("black")
#for eyes
for i in range(-35,105,70):
    emo.up()
    emo.goto(i,35)
    emo.setheading(0)
    emo.down()
    emo.begin_fill()
    emo.circle(10)
    emo.end_fill()
emo.penup()
emo.goto(0,-150)
turtle.mainloop()



