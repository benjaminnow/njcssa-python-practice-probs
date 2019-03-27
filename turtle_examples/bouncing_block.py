

def draw_square(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(4):
        t.forward(size)
        t.right(90)

dy = 0.5
y = 100
x = 100
temp = 0

def next_frame():
    global x, y, dy
    t.clear()
    size = 100

    draw_square(x, y, size)
    if y > screeny:
        dy *= -1
    elif y - size < -screeny:
        dy *= -1
    y += dy
    screen.update()
    screen.ontimer(next_frame, 1)

def stop():
    global dy, temp
    if temp == 0:
        temp = dy
        dy = 0
        print(dy)
    else:
        dy = temp
        temp = 0
        print(dy)



import turtle

t = turtle.Turtle()
screen = turtle.Screen()

t.pensize(3)
t.speed(0)
screen.tracer(0, 0)
t.hideturtle()

screenx = screen.screensize()[0]
screeny = screen.screensize()[1]


next_frame()
screen.onkey(stop, "space")
screen.listen()
screen.mainloop()
    


