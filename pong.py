import turtle
import winsound
import time

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from announcer import Announcer

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
		self.announcer = Announcer()
		self.paddle_a = Paddle(-350, 0)
		self.paddle_b = Paddle(350, 0)
		self.ball = Ball()

		# Keyboard bindings
		self.screen.listen()
		self.screen.onkeypress(self.paddle_a.start_move_up, 'w')
		self.screen.onkeypress(self.paddle_a.start_move_down, 's')
		self.screen.onkeyrelease(self.paddle_a.stop_move_up, 'w')
		self.screen.onkeyrelease(self.paddle_a.stop_move_down, 's')
		self.screen.onkeypress(self.paddle_a.start_long, 'r')
		self.screen.onkeypress(self.paddle_a.prime_fastball, 't')
		self.screen.onkeypress(self.paddle_b.start_move_up, 'Up')
		self.screen.onkeypress(self.paddle_b.start_move_down, 'Down')
		self.screen.onkeyrelease(self.paddle_b.stop_move_up, 'Up')
		self.screen.onkeyrelease(self.paddle_b.stop_move_down, 'Down')
		self.screen.onkeypress(self.paddle_b.start_long, ',')
		self.screen.onkeypress(self.paddle_b.prime_fastball, '.')

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			self._update_paddles()
			self._update_ball()
			self._check_paddle_ball_collision()
			self._check_score()
			self.screen.update()
			time.sleep(1/120)

	def _update_paddles(self):
		"""Update the positions of the paddles."""
		self.paddle_a.update()
		self.paddle_b.update()
	
	def _update_ball(self):
		"""Update the position of the ball."""
		self.ball.move()
		hit_border = self.ball.check_horizontal_borders()
		if hit_border:
			winsound.PlaySound("sounds/bounce.wav", winsound.SND_ASYNC)

	def _check_paddle_ball_collision(self):
		"""Check if a paddle and ball collided."""
		if (self.ball.xcor() < -340 and
			self.ball.xcor() > -350 and
			self.ball.ycor() < self.paddle_a.ycor() + self.paddle_a.hitbox and
			self.ball.ycor() > self.paddle_a.ycor() - self.paddle_a.hitbox):
			self.ball.dx *= -1
			winsound.PlaySound("sounds/bounce.wav", winsound.SND_ASYNC)
			self.ball.increase_speed()
			self.paddle_a.end_long()
			self.paddle_b.end_fastball(self.ball)
			self.paddle_a.start_fastball(self.ball)
		elif (self.ball.xcor() > 340 and
			self.ball.xcor() < 350 and
			self.ball.ycor() < self.paddle_b.ycor() + self.paddle_b.hitbox and
			self.ball.ycor() > self.paddle_b.ycor() - self.paddle_b.hitbox):
			self.ball.dx *= -1
			winsound.PlaySound("sounds/bounce.wav", winsound.SND_ASYNC)
			self.ball.increase_speed()
			self.paddle_b.end_long()
			self.paddle_a.end_fastball(self.ball)
			self.paddle_b.start_fastball(self.ball)
	
	def _check_score(self):
		"""Check if a player scored."""
		if self.ball.xcor() > 410:
			self.sb.increment_a()
		elif self.ball.xcor() < -410:
			self.sb.increment_b()
		else:
			return False
		
		# Reset round only if a player scored.
		self._reset_round()

	def _reset_round(self):
		"""Announce point and reset positions."""
		if self.sb.get_consecutive_points() > 2:
			winsound.PlaySound("sounds/dominating.wav", winsound.SND_ASYNC)
			self.announcer.announce_dominating()
		else:
			winsound.PlaySound("sounds/point_scored.wav", winsound.SND_ASYNC)
			self.announcer.announce_point()
		time.sleep(1)

		# Get ready for next round.
		self.announcer.clear_announcement()
		self.ball.reset_position()
		self.ball.reset_speed()
		self.paddle_a.reset()
		self.paddle_b.reset()


if __name__ == '__main__':
	pong = Pong()
	pong.run_game()
