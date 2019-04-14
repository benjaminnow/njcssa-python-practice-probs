import turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
screen = turtle.Screen()
screen.tracer(0, 0)

#Score
left_score = 0
right_score = 0
# Ball
radius_ball = 10
ballx = 0
bally = 0
normal_speed = 1
dy = normal_speed
dx = normal_speed
# Ball imaginary box
box_x = ballx - radius_ball
box_y = bally + 2*radius_ball
# Border
border_width = 600
border_length = 800
# Paddle
paddle_size = 100  
paddle_width = 10
paddle_l_x = -border_length/2 
paddle_l_y = paddle_size/2
paddle_r_x = border_length/2 - paddle_width
paddle_r_y = paddle_size/2


def draw_score():
    t.penup()
    t.goto(0, 310)
    t.pendown()
    t.write("{}:{}".format(left_score, right_score), font=("Arial", 16, "normal"))


def draw_ball(x,y):
  t.penup()
  t.goto(x,y+radius_ball)
  t.pendown()
  t.circle(radius_ball,360)



def border():
  t.penup()
  t.goto(-border_length/2,border_width/2)
  t.seth(0)
  t.pendown()
  t.forward(border_length)
  t.right(90)
  t.forward(border_width)
  t.right(90)
  t.forward(border_length)
  t.right(90)
  t.forward(border_width)





def paddle_left():
  global paddle_l_y
  t.penup()
  t.goto(paddle_l_x, paddle_l_y)
  t.seth(0)
  t.pendown()
  t.forward(paddle_width)
  t.rt(90)
  t.fd(paddle_size)
  t.rt(90)
  t.fd(paddle_width)
  t.rt(90)
  t.fd(paddle_size)


  

def paddle_right():
  global paddle_r_y
  t.penup()
  t.goto(paddle_r_x, paddle_r_y)
  t.seth(0)
  t.pendown()
  t.forward(paddle_width)
  t.rt(90)
  t.fd(paddle_size)
  t.rt(90)
  t.fd(paddle_width)
  t.rt(90)
  t.fd(paddle_size)



def draw_game():
  t.clear()
  draw_ball(ballx, bally)
  border()
  paddle_left()
  paddle_right()
  draw_score()
  screen.update()
  ball_move()
  wall_collision()
  ai()
  smart_ai()
  screen.ontimer(draw_game, 1)


def ball_move():
  global ballx, bally,box_x,box_y
  ballx = ballx + dx
  bally = bally + dy
  box_x = ballx - radius_ball
  box_y = bally + 2*radius_ball

def wall_collision():
  global dx, dy, ballx, bally, right_score, left_score
  box_r_x = box_x + 2*radius_ball
  paddle_r_lower_y = paddle_r_y - paddle_size

  box_lower_y = box_y - 2*radius_ball
  paddle_l_lower_y = paddle_l_y - paddle_size
  
  # left paddle 
  if box_x <= paddle_l_x + paddle_width*2 and (box_lower_y < paddle_l_y and box_y > paddle_l_lower_y):
    dx = dx * -1
    dx = dx * 1.05
    dy = dy * 1.05
    ballx = paddle_l_x + paddle_width + 2*radius_ball + 1
    print("L")

  # right paddle
  elif box_r_x - radius_ball >= paddle_r_x and (box_lower_y < paddle_r_y  and box_y > paddle_r_lower_y):
    dx = dx * -1
    dx = dx * 1.05
    dy = dy * 1.05
    ballx = paddle_r_x - radius_ball - 1
    print("R")

  # left edge - loss for left
  elif box_x - radius_ball <= -border_length/2:
    #dx = dx * -1
    ballx = 0
    bally = 0
    dx = normal_speed
    dy = normal_speed
    right_score += 1

  # right  - loss for right
  elif box_x + radius_ball >= border_length/2:
    #dx = dx * -1
    ballx = 0
    bally = 0
    dx = normal_speed * -1
    dy = normal_speed * -1
    left_score += 1
    

  #top edge  
  elif box_y >= border_width/2:
    dy = dy * -1
    bally = border_width/2 - 2*radius_ball - 1
  
  #bottom edge
  elif box_y - 2*radius_ball <= -border_width/2:
    dy = dy * -1
    bally = -border_width/2 + 2*radius_ball + 1


def right_paddle_up():
  global paddle_r_y
  if paddle_r_y < border_width/2:
    paddle_r_y += 50
  
def right_paddle_down():
  global paddle_r_y
  if paddle_r_y - paddle_size > -border_width/2:
    paddle_r_y -= 50


def left_paddle_up():
  global paddle_l_y
  if paddle_l_y < border_width/2:
    paddle_l_y += 50

def left_paddle_down():
  global paddle_l_y
  if paddle_l_y - paddle_size > -border_width/2:
    paddle_l_y -= 50


def ai():
    global paddle_l_y, paddle_r_y
    if bally + paddle_size/2 > border_width/2:
        paddle_l_y = border_width/2
        #paddle_r_y = border_width/2
    elif bally + paddle_size/2 - paddle_size <= -border_width/2:
        paddle_l_y = -border_width/2 + paddle_size
        #paddle_r_y = -border_width/2 + paddle_size
    else:
        paddle_l_y = bally + paddle_size/2
        #paddle_r_y = bally + paddle_size/2

################################################################

def get_contact_point(ballx, bally, dx, dy):
    y_intercept = 0
    if dy < 0:
        y_intercept = bally + ballx
        if -border_length/2 + y_intercept > -border_width/2 and -border_length/2 + y_intercept < border_width/2:
            return [border_length/2, -border_length/2 + y_intercept]
        else:
            return [-border_width/2 + y_intercept, -border_width/2, dx, -dy]
    else:
        y_intercept = bally - ballx
        if border_length/2 + y_intercept > -border_width/2 and border_length/2 + y_intercept < border_width/2:
            return [border_length/2, border_length/2 + y_intercept]
        else:
            return [border_width/2 - y_intercept, border_width/2, dx, -dy]
    
    
def smart_ai():
    global paddle_l_y, paddle_r_y
    if dx > 0:
        contact_point = get_contact_point(ballx, bally, dx, dy)
        #print(contact_point)
        while not contact_point[0] == border_length/2:
            contact_point = get_contact_point(contact_point[0], contact_point[1], contact_point[2], contact_point[3])
            #print(contact_point)
            print(contact_point)
        paddle_r_y = contact_point[1] + paddle_size/2
        print(paddle_r_y)
################################################################


  

  
draw_game()
screen.onkey(right_paddle_up, "Up")
screen.onkey(right_paddle_down, "Down")
screen.onkey(left_paddle_up, "w")
screen.onkey(left_paddle_down, "s")
screen.listen()
screen.mainloop()