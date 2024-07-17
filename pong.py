import turtle
# import os
# import pygame

# Game Window
window = turtle.Screen()
window.title("Pong by @DonghaeYi")
window.bgcolor("white")
window.setup(width = 800, height = 600)
window.tracer(0)

# Score
score1 = 0
score2 = 0

# Paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("black")
paddle1.shapesize(stretch_wid = 5, stretch_len = 1)
paddle1.penup()
paddle1.goto(-350, 0)

# Paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("black")
paddle2.shapesize(stretch_wid = 5, stretch_len = 1)
paddle2.penup()
paddle2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1 # Ball Movement Speed and Direction
ball.dy = -0.1

# Score
score = turtle.Turtle()
score.speed(0)
score.color("black")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0  Player 2: 0", align = "center", font = ("Courier", 24, "normal"))

# Audio
# pygame.mixer.init()
# pygame.mixer.music.load("bounce.wav")

# Paddle Movement
def paddle1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)

def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)

def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)

def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)

# Keyboard Input
window.listen()
window.onkeypress(paddle1_up, "w")
window.onkeypress(paddle1_down, "s")
window.onkeypress(paddle2_up, "Up")
window.onkeypress(paddle2_down, "Down")

# Run Game
while True:
    window.update() 

    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Collision
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        # os.system("aplay bounce.wav")
        # pygame.mixer.music.play()
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        # os.system("aplay bounce.wav")
        # pygame.mixer.music.play()

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("Player 1: {}  Player 2: {}".format(score1, score2), align = "center", font = ("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1: {}  Player 2: {}".format(score1, score2), align = "center", font = ("Courier", 24, "normal"))

    # Paddle Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        # os.system("aplay bounce.wav")
        # pygame.mixer.music.play()

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        # os.system("aplay bounce.wav")
        # pygame.mixer.music.play()
