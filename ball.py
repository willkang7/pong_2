from turtle import Turtle
import winsound

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
		self.dx = 0.2
		self.dy = 0.2

	def move(self):
		"""Move the ball."""
		self.setx(self.xcor() + self.dx)
		self.sety(self.ycor() + self.dy)

	def check_horizontal_borders(self):
		"""Check top and bottom borders."""
		if self.ycor() > 290:
			self.sety(290)
			self.dy *= -1
			winsound.PlaySound("sounds/bounce.wav", winsound.SND_ASYNC)
		elif self.ycor() < -290:
			self.sety(-290)
			self.dy *= -1
			winsound.PlaySound("sounds/bounce.wav", winsound.SND_ASYNC)
