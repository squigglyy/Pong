import turtle 
#followed tut by TokyoEdtech for basics and then made my own changes

screen = turtle.Screen()
screen.title("Pong By Squiggly")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

score_1 = 0
score_2 = 0

#player 1
P1 = turtle.Turtle()
P1.speed(0)
P1.shape("square")
P1.color("white")
P1.shapesize(stretch_wid=5, stretch_len=1)
P1.penup()
P1.goto(-350, 0)



#player 2
P2 = turtle.Turtle()
P2.speed(0)
P2.shape("square")
P2.color("white")
P2.shapesize(stretch_wid=5, stretch_len=1)
P2.penup()
P2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")

ball.penup()
ball.goto(0, 0)


ball.dx = 0.15
ball.dy = 0.15

#pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 255)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("courier", 24, "normal"))



#functions
def player1_up():
    y = P1.ycor()
    y += 20
    P1.sety(y)

def player1_down():
    y = P1.ycor()
    y -= 20
    P1.sety(y)

def player2_up():
    y = P2.ycor()
    y += 20
    P2.sety(y)

def player2_down():
    y = P2.ycor()
    y -= 20
    P2.sety(y)
#keyboard binding

screen.listen()
screen.onkeypress(player1_up, "w")
screen.onkeypress(player1_down, "s")
screen.onkeypress(player2_up, "Up")
screen.onkeypress(player2_down, "Down")



while True:
    screen.update()

    #move the ball

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
       ball.goto(0,0)
       ball.dx *= -1
       score_1 += 1
       pen.clear()
       pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("courier", 24, "normal"))

    if ball.xcor() < -390:
       ball.goto(0,0)
       ball.dx *= -1
       score_2 += 1
       pen.clear()
       pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("courier", 24, "normal"))

#player and ball collision

    if (ball.xcor() > 340 and  ball.xcor() < 350) and (ball.ycor() < P2.ycor() + 50 and ball.ycor() > P2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        

    if (ball.xcor() < -340 and  ball.xcor() > -350) and (ball.ycor() < P1.ycor() + 50 and ball.ycor() > P1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
    