import turtle
import winsound

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

class Pong:
	"""Overall class to manage game assets and behavior."""

	def __init__(self):
		"""Initialize the game, and create game resources."""
		self.screen = turtle.Screen()
		self.screen.title("Pong")
		self.screen.bgcolor("black")
		self.screen.setup(width=800, height=600)
		self.screen.tracer(0)

		# Game assets
		self.sb = Scoreboard()
		self.paddle_a = Paddle(-350, 0)
		self.paddle_b = Paddle(350, 0)
		self.ball = Ball()

		# Keyboard bindings
		self.screen.listen()
		self.screen.onkeypress(self.paddle_a.move_up, "w")
		self.screen.onkeypress(self.paddle_a.move_down, "s")
		self.screen.onkeypress(self.paddle_b.move_up, "Up")
		self.screen.onkeypress(self.paddle_b.move_down, "Down")

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			self.screen.update()
			self._update_ball()
			self._check_score()
			self._check_paddle_ball_collision()

	def _update_ball(self):
		"""Update the position of the ball."""
		self.ball.move()
		self.ball.check_horizontal_borders()

	def _check_score(self):
		"""Check if a player scored."""
		if self.ball.xcor() > 350:
			self.sb.increment_a()
			self.ball.reset()
		elif self.ball.xcor() < -350:
			self.sb.increment_b()
			self.ball.reset()

	def _check_paddle_ball_collision(self):
		"""Check if a paddle and ball collided."""
		if (self.ball.xcor() < -340 and
			self.ball.ycor() < self.paddle_a.ycor() + 50 and
			self.ball.ycor() > self.paddle_a.ycor() - 50):
			self.ball.dx *= -1 
			winsound.PlaySound("sounds/bounce.wav", winsound.SND_ASYNC)
		elif (self.ball.xcor() > 340 and
			self.ball.ycor() < self.paddle_b.ycor() + 50 and
			self.ball.ycor() > self.paddle_b.ycor() - 50):
			self.ball.dx *= -1
			winsound.PlaySound("sounds/bounce.wav", winsound.SND_ASYNC)


if __name__ == '__main__':
	pong = Pong()
	pong.run_game()
