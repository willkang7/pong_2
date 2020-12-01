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

	def move_up(self):
		"""Move the paddle up."""
		y = self.ycor() + 20
		self.sety(y)

	def move_down(self):
		"""Move the paddle down."""
		y = self.ycor() - 20
		self.sety(y)