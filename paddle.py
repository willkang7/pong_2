from turtle import Turtle

class Paddle(Turtle):
	"""A model of a paddle."""

	def __init__(self, x, y):
		"""Initialize the paddle."""
		super().__init__()
		self.speed(0)
		self.shape("square")
		self.color("white")
		self.shapesize(stretch_wid=5,stretch_len=1)
		self.penup()
		self.goto(x, y)
		self.moving_up = False
		self.moving_down = False
		self.speed = 3
		self.hitbox = 50
		self.specials_left = 3
		self.is_long = False
		self.is_fastball = False

	def update(self):
		"""Move the paddle based on the movement flags."""
		if self.moving_up and self.ycor() < 300:
			y = self.ycor() + self.speed
			self.sety(y)
		if self.moving_down and self.ycor() > -300:
			y = self.ycor() - self.speed
			self.sety(y)

	def start_move_up(self):
		"""Move the paddle up."""
		self.moving_up = True

	def start_move_down(self):
		"""Move the paddle down."""
		self.moving_down = True

	def stop_move_up(self):
		"""Stop moving the paddle up."""
		self.moving_up = False

	def stop_move_down(self):
		"""Stop moving the paddle down."""
		self.moving_down = False

	def reset(self):
		"""Reset the position and specials."""
		self.sety(0)
		self.end_long()
		self.specials_left = 3

	def get_hitbox(self):
		"""Return the hitbox value."""
		return self.hitbox

	def start_long(self):
		"""Lengthen the board."""
		if self.specials_left > 0 and self.is_long == False:
			self.is_long = True
			self.shapesize(stretch_wid=10, stretch_len=1)
			self.hitbox = 100
			self.specials_left -= 1

	def end_long(self):
		"""Shorten the board."""
		self.is_long = False
		self.shapesize(stretch_wid=5, stretch_len=1)
		self.hitbox = 50

	def prime_fastball(self):
		"""Prepare to move the ball straight forwards."""
		if self.specials_left > 0 and self.is_fastball == False:
			self.is_fastball = True
			self.specials_left -= 1

	def start_fastball(self, ball):
		"""Move the ball straight forwards."""
		if self.is_fastball == True:
			ball.dy = 0

	def end_fastball(self, ball):
		"""Move the ball normally."""
		if self.is_fastball == True:
			self.is_fastball = False
			ball.dy = ball.dx
