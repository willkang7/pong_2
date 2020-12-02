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
