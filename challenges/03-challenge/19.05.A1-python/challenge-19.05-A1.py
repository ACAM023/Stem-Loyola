'''
 * Copyright: STEM Loyola
 * Date     : May 2019
 * ID       : 19.05-A1
 * Level    : 1 (Beginner)
 *
 * Task     : This is a multipart challenge. In the first part, you are given a
 *            moving ball and your task is to restrict its position within the
 *            screen window (width=800, height=600), hence creating the bouncing
 *            illusion.
 *
 *            Note: A video tutorial is available to support solving this
 *                  challenge.
 *
 * Solved By: <Full Name> - <Email Address>
 *     Class: <Form> - <Stream/Combination>
'''

from turtle import *
import time

# Store important values
screenHeight = 600
screenWidth = 900
ballSize = 25
wallSize = 25
gravity = -0.05

# Create a screen variable and setup the screen window
screen = Screen()
screen.setup(screenWidth, screenHeight)
screen.tracer(0)    # Stop auto updating screen window. We will manually update
screen.title("Loyola STEM: Challenge #3 Solved by [Alvin]")
screen.bgpic("background.gif")

# Create a ball shape and setup its color and size
ball = Turtle()
ball.speed(0)
ball.penup()
ball.shape("circle")
ball.color("red")
ball.turtlesize(2)

# Define how fast the ball will be moving vertically and horizontally
ball.speedX = 2
ball.speedY = 3

# Since we want the ball to keep on moving forever (until we close our program),
# we are going to use a loop. Refer to the support video for more details.
while True:
    time.sleep(0.01)   # Pauses the program for 0.01 seconds so we can see the ball moving smoothly
    screen.update()    # Manually update the screen (i.e. clear and redraw everything)
        
    # Get the current ball location and calculate its new location.
    currentX = ball.xcor()
    currentY = ball.ycor()
    
    newX = currentX + ball.speedX
    newY = currentY + ball.speedY + gravity
    
    # Update the ball location
    ball.setx(newX)
    ball.sety(newY)
    
    # Check if the new location (newX or newY) is outside the screen dimensions
    # If it is, change the direction of its respective speed (i.e. if the speed
    # was positive, it has to be negative, if it was negative it has to be
    # positive. This will ensure, if the ball was moving horizontally to the left
    # (negative horizontal speed) and reaches the left wall, it will start moving
    # towards the right (positive horizontal speed) and create the illusion that
    # the ball has bounced on the left wall.
    # Add your code below
    
    if newY >= 250 or newY <= -250:
        ball.speedY = -ball.speedY
        
    if newX >= 400 or newX <= -400:
        ball.speedX = -ball.speedX
    