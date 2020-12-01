import turtle
import winsound

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
sb = Scoreboard()

# Paddle A
paddle_a = Paddle(-350, 0)

# Paddle B
paddle_b = Paddle(350, 0)

# Ball
ball = Ball()

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a.move_up, "w")
wn.onkeypress(paddle_a.move_down, "s")
wn.onkeypress(paddle_b.move_up, "Up")
wn.onkeypress(paddle_b.move_down, "Down")

# Main game loop
while True:
	wn.update()
	
	# Move the ball.
	ball.move()

	# Check if the ball hit top or bottom.
	ball.check_horizontal_borders()

	# Check if a player scored.
	if ball.xcor() > 350:
		sb.increment_a()
		ball.reset()
	elif ball.xcor() < -350:
		sb.increment_b()
		ball.reset()

	# Paddle and ball collisions
	if (ball.xcor() < -340 and
		ball.ycor() < paddle_a.ycor() + 50 and
		ball.ycor() > paddle_a.ycor() - 50):
		ball.dx *= -1 
		winsound.PlaySound("sounds/bounce.wav", winsound.SND_ASYNC)
	elif (ball.xcor() > 340 and
		ball.ycor() < paddle_b.ycor() + 50 and
		ball.ycor() > paddle_b.ycor() - 50):
		ball.dx *= -1
		winsound.PlaySound("sounds/bounce.wav", winsound.SND_ASYNC)
