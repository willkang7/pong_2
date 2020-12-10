from turtle import Turtle

class Ball(Turtle):
	"""A model of a ball."""

	def __init__(self):
		"""Initialize the ball."""
		super().__init__()
		self.speed(0)
		self.shape("square")
		self.color("white")
		self.penup()
		self.goto(0, 0)
		self.dx = 2
		self.dy = 2

	def move(self):
		"""Move the ball."""
		self.setx(self.xcor() + self.dx)
		self.sety(self.ycor() + self.dy)

	def check_horizontal_borders(self):
		"""Check top and bottom borders."""
		if self.ycor() > 290:
			self.sety(290)
			self.dy *= -1
			return True
		elif self.ycor() < -290:
			self.sety(-290)
			self.dy *= -1
			return True
		return False

	def reset_position(self):
		"""Reset the ball to the center."""
		self.goto(0, 0)
		self.dx *= -1

	def increase_speed(self):
		"""Increase ball speed."""
		self.dx *= 1.1
		self.dy *= 1.1

	def reset_speed(self):
		"""Reset ball speed."""
		self.dx = 2
		self.dy = 2
